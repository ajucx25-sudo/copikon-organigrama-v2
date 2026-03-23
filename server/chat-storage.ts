import { drizzle } from "drizzle-orm/better-sqlite3";
import Database from "better-sqlite3";
import { eq, and, or, desc, ne } from "drizzle-orm";
import { users, messages, type User, type InsertUser, type Message, type InsertMessage } from "@shared/schema";

const sqlite = new Database("chat.db");
export const db = drizzle(sqlite);

// Auto-migrate
sqlite.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    nombre TEXT NOT NULL,
    cargo TEXT NOT NULL,
    gerencia TEXT NOT NULL,
    cargo_id TEXT NOT NULL,
    online INTEGER NOT NULL DEFAULT 0,
    last_seen TEXT,
    created_at TEXT NOT NULL
  );
  CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_id INTEGER NOT NULL,
    to_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL,
    read INTEGER NOT NULL DEFAULT 0
  );
`);

export interface IStorage {
  // Users
  createUser(data: InsertUser): User;
  getUserByUsername(username: string): User | undefined;
  getUserById(id: number): User | undefined;
  getAllUsers(): User[];
  setOnline(id: number, online: boolean): void;

  // Messages
  sendMessage(data: InsertMessage): Message;
  getConversation(userId1: number, userId2: number): Message[];
  markRead(fromId: number, toId: number): void;
  getUnreadCount(toId: number): Record<number, number>;
  getLastMessages(userId: number): { otherId: number; message: Message }[];
}

export class Storage implements IStorage {
  createUser(data: InsertUser): User {
    return db.insert(users).values({
      ...data,
      online: false,
      createdAt: new Date().toISOString(),
    }).returning().get()!;
  }

  getUserByUsername(username: string): User | undefined {
    return db.select().from(users).where(eq(users.username, username)).get();
  }

  getUserById(id: number): User | undefined {
    return db.select().from(users).where(eq(users.id, id)).get();
  }

  getAllUsers(): User[] {
    return db.select().from(users).all();
  }

  setOnline(id: number, online: boolean): void {
    db.update(users).set({
      online,
      lastSeen: new Date().toISOString(),
    }).where(eq(users.id, id)).run();
  }

  sendMessage(data: InsertMessage): Message {
    return db.insert(messages).values({
      ...data,
      read: false,
      createdAt: new Date().toISOString(),
    }).returning().get()!;
  }

  getConversation(userId1: number, userId2: number): Message[] {
    return db.select().from(messages).where(
      or(
        and(eq(messages.fromId, userId1), eq(messages.toId, userId2)),
        and(eq(messages.fromId, userId2), eq(messages.toId, userId1)),
      )
    ).orderBy(messages.createdAt).all();
  }

  markRead(fromId: number, toId: number): void {
    db.update(messages).set({ read: true })
      .where(and(eq(messages.fromId, fromId), eq(messages.toId, toId))).run();
  }

  getUnreadCount(toId: number): Record<number, number> {
    const rows = db.select().from(messages)
      .where(and(eq(messages.toId, toId), eq(messages.read, false))).all();
    const counts: Record<number, number> = {};
    for (const r of rows) {
      counts[r.fromId] = (counts[r.fromId] || 0) + 1;
    }
    return counts;
  }

  getLastMessages(userId: number): { otherId: number; message: Message }[] {
    const all = db.select().from(messages).where(
      or(eq(messages.fromId, userId), eq(messages.toId, userId))
    ).orderBy(desc(messages.createdAt)).all();

    const seen = new Set<number>();
    const result: { otherId: number; message: Message }[] = [];
    for (const m of all) {
      const otherId = m.fromId === userId ? m.toId : m.fromId;
      if (!seen.has(otherId)) {
        seen.add(otherId);
        result.push({ otherId, message: m });
      }
    }
    return result;
  }
}

export const storage = new Storage();
