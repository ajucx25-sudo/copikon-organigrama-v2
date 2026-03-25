#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera manuales y flujos para los 7 cargos de Renta Impresora y Gestión Documental - Copikon Venezuela
"""
import json, os

# ─────────────────────────────────────────────────────────────────────────────
# MANUALES
# ─────────────────────────────────────────────────────────────────────────────

MANUAL_COORDINADOR = """MANUAL DE PROCEDIMIENTO — Coordinador Comercial Renta Impresora y Gestión Documental

1. OBJETIVO
Liderar la estrategia comercial del área de Renta de Impresoras Ricoh y Gestión Documental en las tres regiones operativas de Copikon Venezuela, garantizando el cumplimiento de metas de ventas, la correcta ejecución de contratos marco y la satisfacción integral del cliente.

2. ALCANCE
Aplica a todas las actividades comerciales, contractuales, de supervisión y de relacionamiento con Ricoh Venezuela y clientes corporativos en las regiones Caracas, Centro (Aragua, Carabobo) y Occidente (Lara, Portuguesa, Yaracuy).

3. PROCEDIMIENTOS PRINCIPALES

3.1 Gestión Estratégica del Portafolio
- Revisar mensualmente el portafolio de contratos activos de renta de impresoras y servicios de gestión documental por región.
- Definir con la gerencia las metas trimestrales de ventas nuevas, renovaciones y expansión de servicios.
- Coordinar con Ricoh Venezuela la disponibilidad de equipos multifuncionales, condiciones de precios y campañas comerciales vigentes.
- Actualizar el catálogo interno de planes CPP (costo por página), opciones de suministros y servicios de gestión documental.
- Presentar informe ejecutivo mensual a la gerencia con resultados por región y proyección de ingresos.

3.2 Supervisión del Equipo Comercial
- Realizar reuniones de seguimiento semanales con los tres analistas comerciales regionales.
- Revisar y aprobar propuestas comerciales para contratos de renta superiores a 10 equipos o con condiciones especiales de precio.
- Definir criterios de segmentación de clientes (pymes, corporativos, sector público) y asignar cuentas estratégicas.
- Evaluar el desempeño mensual de analistas y vendedores mediante revisión de KPIs de pipeline, cierre y satisfacción.
- Brindar coaching individualizado a analistas y vendedores con bajo rendimiento.

3.3 Gestión de Contrato Marco con Ricoh
- Mantener actualizado el contrato marco de distribución y servicio técnico con Ricoh Venezuela.
- Negociar condiciones de garantías, tiempos de respuesta de mantenimiento correctivo y niveles de stock de tóner.
- Coordinar auditorías técnicas de equipos instalados al menos una vez por semestre.
- Gestionar créditos, notas de entrega y devoluciones de equipos defectuosos con el proveedor Ricoh.
- Asegurar el cumplimiento de las certificaciones técnicas requeridas por Ricoh para los técnicos de Copikon.

3.4 Planificación de Ventas y Renovaciones
- Generar y mantener actualizado el calendario de vencimiento de contratos con 90 días de anticipación.
- Coordinar con los analistas la estrategia de renovación o upselling en contratos por vencer.
- Aprobar descuentos y condiciones especiales en negociaciones de renovación de alto valor.
- Revisar y validar la correcta facturación de conteos de páginas (CPP) mensual con cada cliente.
- Asegurar que los clientes sin contrato activo sean atendidos con propuesta de formalización en un plazo máximo de 15 días hábiles.

4. KPIs DEL CARGO
- Tasa de renovación de contratos: ≥ 85% de contratos vigentes renovados al vencimiento
- Crecimiento mensual de equipos instalados (fleet): ≥ 5% intermensual por región
- Tiempo promedio de resolución de reclamos técnicos escalados: ≤ 48 horas
- Cumplimiento de meta de ventas nuevas (contratos renta + gestión documental): ≥ 90% del objetivo trimestral
- Satisfacción del cliente (NPS o encuesta post-instalación): ≥ 80 puntos

5. DOCUMENTOS Y SISTEMAS
- Contrato Marco Ricoh Venezuela (versión vigente)
- CRM corporativo Copikon (pipeline, oportunidades, contratos)
- Plantillas de propuesta comercial de renta CPP y gestión documental
- Informe mensual de conteo de páginas por cliente
- Sistema de gestión documental Copikon (módulo contratos)
- Calendario de vencimientos de contratos (Excel / CRM)
- Política de descuentos y condiciones comerciales aprobadas"""

MANUAL_ANALISTA_CARACAS = """MANUAL DE PROCEDIMIENTO — Analista Comercial Renta Impresora y Gestión Documental (Caracas)

1. OBJETIVO
Gestionar el pipeline comercial de la región Caracas para los servicios de renta de impresoras Ricoh y gestión documental, asegurando la prospección activa, elaboración de propuestas, cierre de contratos y seguimiento de renovaciones en la zona asignada.

2. ALCANCE
Aplica a todas las cuentas y oportunidades comerciales activas e inactivas ubicadas en el Área Metropolitana de Caracas y municipios adyacentes asignados por el Coordinador Comercial.

3. PROCEDIMIENTOS PRINCIPALES

3.1 Gestión del Pipeline Comercial
- Registrar y actualizar diariamente todas las oportunidades activas en el CRM, indicando etapa, valor estimado y fecha de cierre proyectada.
- Priorizar las oportunidades según criterio de valor del contrato, probabilidad de cierre y segmento de cliente.
- Coordinar con el vendedor de Caracas la agenda de visitas y demostraciones de equipos Ricoh.
- Hacer seguimiento a las propuestas enviadas con llamadas o correos a los 2, 5 y 10 días hábiles.
- Reportar al coordinador el avance semanal del pipeline con proyección de cierres del mes.

3.2 Elaboración de Propuestas Comerciales
- Levantar los requerimientos del cliente (volumen de impresión, tipo de documentos, necesidades de gestión documental) junto con el vendedor de campo.
- Calcular el plan CPP adecuado según el volumen estimado de páginas mensuales (blanco/negro y color).
- Elaborar la propuesta formal de renta en la plantilla corporativa incluyendo: modelo de equipo Ricoh, plan CPP, suministros incluidos, SLA de mantenimiento y opciones de gestión documental.
- Obtener aprobación del coordinador para propuestas con descuentos superiores al 10% o condiciones especiales.
- Enviar la propuesta al cliente y confirmar recepción en un plazo máximo de 24 horas hábiles.

3.3 Cierre de Contratos y Onboarding
- Coordinar con el área legal/administrativa la generación del contrato de arrendamiento de equipos Ricoh.
- Verificar que el contrato incluya: identificación del equipo, plan CPP, fecha de inicio, duración, condiciones de mantenimiento y cláusulas de terminación anticipada.
- Acompañar al cliente durante la firma del contrato y resolver dudas sobre términos y condiciones.
- Notificar al equipo técnico la fecha de instalación y datos de ubicación del cliente.
- Realizar llamada de bienvenida al cliente a los 7 días de instalación para confirmar satisfacción.

3.4 Seguimiento de Renovaciones y Cuentas Activas
- Monitorear mensualmente el estado de uso (páginas impresas vs. plan contratado) de cada cliente activo.
- Alertar al coordinador y al cliente cuando el consumo supere el 90% del plan mensual contratado.
- Iniciar gestión de renovación con 60 días de anticipación al vencimiento del contrato.
- Documentar cualquier reclamo del cliente (equipos, suministros, facturación) y hacer seguimiento hasta su resolución.
- Identificar oportunidades de upselling (más equipos, mayor plan CPP, incorporación de gestión documental) en cuentas activas.

4. KPIs DEL CARGO
- Número de nuevos contratos de renta cerrados por mes: ≥ 5 contratos
- Tasa de conversión de propuestas enviadas a contratos firmados: ≥ 30%
- Tasa de renovación de contratos Caracas: ≥ 85%
- Tiempo promedio de elaboración y envío de propuesta desde levantamiento: ≤ 2 días hábiles
- Actualización del CRM: 100% de oportunidades activas registradas y actualizadas

5. DOCUMENTOS Y SISTEMAS
- CRM corporativo Copikon (módulo pipeline y contratos)
- Plantilla de propuesta comercial CPP (Excel/PDF corporativo)
- Tarifario de planes CPP Ricoh vigente
- Contrato estándar de arrendamiento de equipos (Word/PDF)
- Sistema de gestión documental Copikon
- Informe mensual de páginas por cliente (reportado por técnicos)
- Base de datos de clientes Caracas (CRM)"""

MANUAL_ANALISTA_ARAGUA_CARABOBO = """MANUAL DE PROCEDIMIENTO — Analista Comercial Renta Impresora y Gestión Documental (Aragua, Carabobo)

1. OBJETIVO
Gestionar el pipeline comercial de la región centro (Aragua y Carabobo) para los servicios de renta de impresoras Ricoh y gestión documental, garantizando la prospección, elaboración de propuestas, cierre de contratos y fidelización de clientes en la zona asignada.

2. ALCANCE
Aplica a todas las oportunidades y cuentas activas ubicadas en los estados Aragua y Carabobo, incluyendo los municipios y parques industriales asignados por el Coordinador Comercial.

3. PROCEDIMIENTOS PRINCIPALES

3.1 Gestión del Pipeline Regional Centro
- Mantener actualizado el CRM con todas las oportunidades activas de Aragua y Carabobo, con etapa, monto estimado y próxima acción.
- Planificar con el vendedor de región centro la agenda semanal de visitas, demos y seguimientos presenciales.
- Analizar el potencial comercial de los parques industriales y zonas empresariales de Maracay y Valencia para identificar prospectos nuevos.
- Enviar reporte semanal de pipeline al coordinador con estado de oportunidades y forecast del mes.
- Coordinar con logística la disponibilidad de equipos Ricoh para demostraciones en la región.

3.2 Elaboración y Gestión de Propuestas
- Levantar con el vendedor de campo los requerimientos técnicos del cliente (volumen, tipo de impresión, documentos físicos a digitalizar).
- Estructurar la propuesta CPP incluyendo modelo de equipo, suministros, SLA de mantenimiento y opciones de digitalización/gestión documental.
- Adaptar las propuestas al contexto industrial de la región (manufactura, agroindustria, comercio), destacando beneficios de automatización documental.
- Gestionar aprobaciones internas y enviar propuesta al cliente con seguimiento activo.
- Registrar resultado de cada propuesta (ganada, perdida, en negociación) en el CRM con notas de motivo.

3.3 Cierre y Formalización de Contratos
- Coordinar con administración la emisión del contrato de arrendamiento revisando condiciones pactadas en la propuesta.
- Verificar disponibilidad del equipo Ricoh y coordinar logística de transporte y fecha de instalación en la región centro.
- Asegurar la firma del contrato por el representante autorizado del cliente y el representante de Copikon.
- Notificar al equipo técnico de la región con mínimo 5 días hábiles de anticipación a la instalación.
- Realizar seguimiento post-instalación a los 7 y 30 días para verificar satisfacción y funcionamiento del equipo.

3.4 Renovaciones y Expansión de Cartera
- Revisar mensualmente el listado de contratos por vencer en los próximos 90 días en Aragua y Carabobo.
- Contactar proactivamente a los clientes con contratos por vencer para iniciar negociación de renovación.
- Identificar oportunidades de expansión (equipos adicionales, digitalización de archivos físicos, software de gestión documental).
- Documentar y escalar al coordinador las cuentas en riesgo de no renovar con plan de retención.
- Actualizar el historial de interacciones con cada cliente en el CRM tras cada contacto.

4. KPIs DEL CARGO
- Nuevos contratos de renta cerrados por mes en la región centro: ≥ 4 contratos
- Tasa de conversión de propuestas a contratos: ≥ 30%
- Tasa de renovación contratos Aragua-Carabobo: ≥ 85%
- Tiempo de respuesta en elaboración de propuesta desde levantamiento: ≤ 2 días hábiles
- Cobertura de prospectos nuevos identificados por mes: ≥ 10 prospectos nuevos ingresados al CRM

5. DOCUMENTOS Y SISTEMAS
- CRM corporativo Copikon (pipeline, contratos, historial de clientes)
- Tarifario CPP Ricoh vigente por modelo de equipo
- Plantilla de propuesta comercial corporativa
- Contrato estándar de arrendamiento de equipos Ricoh
- Sistema de gestión documental Copikon
- Mapa de cobertura y segmentación de clientes Aragua-Carabobo
- Informe mensual de conteo de páginas de clientes activos"""

MANUAL_ANALISTA_LARA = """MANUAL DE PROCEDIMIENTO — Analista Comercial Renta Impresora y Gestión Documental (Lara, Portuguesa, Yaracuy)

1. OBJETIVO
Gestionar el pipeline comercial de la región occidente (Lara, Portuguesa y Yaracuy) para los servicios de renta de impresoras Ricoh y gestión documental, asegurando la captación de nuevos clientes, el cierre de contratos y la fidelización de la cartera activa en la zona.

2. ALCANCE
Aplica a todas las oportunidades y cuentas activas en los estados Lara, Portuguesa y Yaracuy, con énfasis en los sectores agroindustrial, comercial e institucional predominantes en la región.

3. PROCEDIMIENTOS PRINCIPALES

3.1 Prospección y Gestión del Pipeline Occidente
- Identificar y registrar en el CRM al menos 10 nuevos prospectos mensuales en la región (Lara, Portuguesa, Yaracuy).
- Coordinar con el vendedor regional la ruta de visitas semanales optimizando distancias entre municipios.
- Analizar el potencial de clientes en los sectores agroindustrial (Portuguesa), comercio (Barquisimeto) e institucional (alcaldías, hospitales).
- Reportar semanalmente al coordinador el avance del pipeline con detalle de oportunidades por estado y etapa.
- Gestionar la logística de traslado de equipos Ricoh para demostraciones en zonas remotas de la región.

3.2 Elaboración de Propuestas Adaptadas a la Región
- Levantar con el vendedor los requerimientos específicos del cliente incluyendo infraestructura eléctrica, conectividad y volumen de impresión.
- Considerar las particularidades logísticas de la región (distancias, vías) al proponer SLA de mantenimiento correctivo.
- Elaborar propuestas CPP que incluyan opciones de digitalización de documentos especialmente para empresas agropecuarias con grandes volúmenes de registros físicos.
- Presentar opciones de gestión documental electrónica como diferenciador frente a la competencia en mercados menos saturados.
- Enviar la propuesta y hacer seguimiento estructurado a los 2, 5 y 10 días hábiles.

3.3 Cierre de Contratos y Coordinación Logística
- Coordinar con administración y logística la emisión del contrato y el transporte del equipo Ricoh desde el almacén hasta la ubicación del cliente.
- Verificar condiciones de instalación (espacio, conexión eléctrica, red) con el cliente antes de despachar el equipo.
- Asegurar la firma del contrato de arrendamiento por las partes y su registro en el sistema de gestión documental.
- Acompañar o delegar al vendedor el proceso de instalación y capacitación básica al usuario del equipo.
- Confirmar funcionamiento correcto del equipo y del plan CPP en el sistema a los 2 días hábiles de instalación.

3.4 Gestión de Cartera Activa y Renovaciones
- Monitorear mensualmente el uso de páginas de cada cliente activo en la región para detectar sobre o subuso del plan.
- Proponer ajuste de plan CPP al cliente cuando el consumo difiera más del 20% del plan contratado por 2 meses consecutivos.
- Iniciar gestión de renovación a los 60 días previos al vencimiento del contrato.
- Gestionar reclamos de clientes (suministros, fallas técnicas, facturación) coordinando con soporte técnico y administración.
- Documentar en el CRM cada interacción con el cliente y el resultado de la gestión.

4. KPIs DEL CARGO
- Nuevos contratos cerrados por mes en región occidente: ≥ 3 contratos
- Tasa de conversión propuestas a contratos: ≥ 28%
- Tasa de renovación contratos Lara-Portuguesa-Yaracuy: ≥ 83%
- Tiempo promedio de entrega de propuesta desde levantamiento: ≤ 3 días hábiles (considerando distancias)
- Clientes activos con consumo monitoreado mensualmente: 100%

5. DOCUMENTOS Y SISTEMAS
- CRM corporativo Copikon (pipeline, historial de clientes, contratos)
- Tarifario CPP Ricoh vigente
- Plantilla de propuesta comercial corporativa
- Contrato estándar de arrendamiento de equipos Ricoh
- Sistema de gestión documental Copikon
- Guía de SLA de mantenimiento por distancia/región
- Mapa de cobertura región occidente (Lara, Portuguesa, Yaracuy)"""

MANUAL_VENDEDOR_CARACAS = """MANUAL DE PROCEDIMIENTO — Vendedor Renta Impresora y Gestión Documental (Caracas)

1. OBJETIVO
Ejecutar la prospección de campo, demostraciones de equipos Ricoh, levantamiento de necesidades de gestión documental y cierre de ventas en la región Caracas, generando oportunidades calificadas para el equipo comercial de Copikon Venezuela.

2. ALCANCE
Aplica a todas las actividades de venta de campo realizadas en el Área Metropolitana de Caracas y municipios adyacentes asignados, incluyendo visitas a prospectos, clientes activos y demostraciones técnicas.

3. PROCEDIMIENTOS PRINCIPALES

3.1 Prospección y Ruta Diaria de Campo
- Planificar diariamente la ruta de visitas con base en el listado de prospectos y clientes asignados por el analista comercial.
- Realizar un mínimo de 6 visitas presenciales diarias a prospectos fríos, tibios o clientes activos.
- Registrar el resultado de cada visita en el CRM al finalizar la jornada (contacto realizado, interés, próxima acción).
- Capturar datos de contacto del decisor de compra (gerente administrativo, director de operaciones, dueño) en cada visita.
- Coordinar con el analista comercial la priorización de visitas según el avance del pipeline semanal.

3.2 Demostración de Equipos Ricoh
- Preparar el equipo Ricoh de demostración verificando que esté limpio, funcional y con suministros suficientes.
- Trasladar el equipo de demostración al cliente o coordinar una visita a la sala de exhibición de Copikon.
- Ejecutar la demostración mostrando funciones clave: impresión, copiado, escaneo, envío digital de documentos y opciones de gestión documental.
- Destacar los beneficios del plan CPP (costo fijo, mantenimiento incluido, suministros incluidos) versus la compra directa del equipo.
- Resolver dudas técnicas básicas del cliente y escalar al analista o al equipo técnico las preguntas específicas.

3.3 Levantamiento de Necesidades de Gestión Documental
- Aplicar el cuestionario de levantamiento de necesidades documentales en cada visita a prospectos con alto volumen de papel.
- Identificar el volumen estimado de documentos físicos a digitalizar, tipos de documentos (facturas, expedientes, contratos) y flujos de aprobación actuales.
- Documentar las necesidades en el formato de levantamiento y trasladar la información al analista comercial para la elaboración de propuesta.
- Presentar brevemente las capacidades del software de gestión documental de Copikon (digitalización, indexación, flujos electrónicos).
- Identificar si el cliente tiene urgencia regulatoria (auditorías, requisitos SENIAT) que acelere la decisión de compra.

3.4 Cierre y Seguimiento Post-Venta
- Apoyar al analista comercial durante la presentación de la propuesta al cliente cuando se requiera presencia de campo.
- Gestionar objeciones comerciales frecuentes (precio, duración del contrato, comparación con otras marcas) con los argumentos de venta aprobados.
- Notificar al analista cuando el cliente emita señales de cierre (solicitud de contrato, aprobación interna, solicitud de segunda demo).
- Estar presente durante la instalación del equipo para reforzar la relación con el cliente y garantizar una experiencia positiva.
- Realizar visita de seguimiento al cliente a los 30 días de instalación para detectar necesidades adicionales y oportunidades de upselling.

4. KPIs DEL CARGO
- Visitas de campo realizadas por semana: ≥ 30 visitas
- Oportunidades calificadas generadas por mes (registradas en CRM): ≥ 15 oportunidades
- Demostraciones de equipos Ricoh realizadas por mes: ≥ 8 demostraciones
- Tasa de conversión de visita a oportunidad calificada: ≥ 25%
- Levantamientos de gestión documental completados por mes: ≥ 5 levantamientos

5. DOCUMENTOS Y SISTEMAS
- CRM corporativo Copikon (registro de visitas, oportunidades)
- Formulario de levantamiento de necesidades de gestión documental
- Guía de argumentos de venta y manejo de objeciones (renta Ricoh)
- Catálogo de equipos Ricoh multifuncionales y planes CPP
- Presentación corporativa Copikon (Renta + Gestión Documental)
- Equipo Ricoh de demostración (asignado al vendedor)
- Aplicación móvil CRM (registro inmediato en campo)"""

MANUAL_VENDEDOR_ARAGUA_CARABOBO = """MANUAL DE PROCEDIMIENTO — Vendedor Renta Impresora y Gestión Documental (Aragua, Carabobo)

1. OBJETIVO
Ejecutar la venta de campo, demostraciones de equipos Ricoh y levantamiento de necesidades de gestión documental en los estados Aragua y Carabobo, generando oportunidades calificadas y apoyando el cierre de contratos en la región centro.

2. ALCANCE
Aplica a todas las actividades de venta presencial realizadas en los estados Aragua y Carabobo, cubriendo parques industriales, centros comerciales, instituciones y empresas de los principales municipios (Maracay, Valencia, La Victoria, Güigüe, entre otros).

3. PROCEDIMIENTOS PRINCIPALES

3.1 Prospección y Ruta de Campo en Región Centro
- Planificar semanalmente la ruta de visitas en Aragua y Carabobo coordinando con el analista comercial la priorización de zonas.
- Realizar un mínimo de 5 visitas presenciales diarias a prospectos y clientes activos en la región.
- Enfocar la prospección en parques industriales (Zona Industrial Valencia, Parque Industrial Maracay) donde el volumen de impresión es elevado.
- Registrar resultados de visitas en el CRM al final de cada jornada con detalles del contacto y próxima acción.
- Reportar al analista comercial cualquier oportunidad calificada identificada en el día para incluirla en el pipeline regional.

3.2 Demostraciones de Equipos Ricoh en la Región
- Coordinar con el analista el traslado del equipo de demostración desde el punto de almacenamiento regional al cliente.
- Ejecutar demostraciones de los modelos Ricoh más adecuados al perfil del cliente industrial (volumen alto, funciones de escaneo masivo, conectividad en red).
- Resaltar la continuidad operativa que garantiza el contrato de renta (mantenimiento preventivo y correctivo, suministros incluidos).
- Realizar comparativo básico de costo total de propiedad (compra vs. renta CPP) para clientes con equipos propios en mal estado.
- Coordinar visitas a la oficina o showroom de Copikon en Valencia o Maracay cuando el cliente prefiera ver los equipos en exhibición.

3.3 Levantamiento Documental en Empresas Industriales
- Aplicar el formulario de levantamiento de necesidades documentales con énfasis en empresas de manufactura y agroindustria.
- Identificar volúmenes de facturas, guías de despacho, órdenes de compra y expedientes de RRHH que puedan ser digitalizados.
- Documentar los flujos de aprobación actuales (firmas físicas, traslado de documentos entre plantas) para proponer flujos electrónicos equivalentes.
- Trasladar el formulario completo al analista para elaborar la propuesta de gestión documental integrada.
- Presentar brevemente casos de éxito de empresas similares en la región que ya usan el servicio de Copikon.

3.4 Apoyo al Cierre y Postventa
- Participar activamente en la reunión de presentación de propuesta cuando el analista requiera soporte de campo.
- Gestionar objeciones de precio y tiempo de contrato usando los argumentos de venta corporativos y el manual de objeciones.
- Coordinar con logística y el analista la fecha y condiciones de instalación del equipo en la planta o sede del cliente.
- Estar presente en la instalación para asegurar la relación con el usuario final del equipo (operador, asistente administrativo).
- Realizar visita de seguimiento a los 15 y 30 días post-instalación para detectar necesidades adicionales.

4. KPIs DEL CARGO
- Visitas de campo por semana en región centro: ≥ 25 visitas
- Oportunidades calificadas generadas por mes: ≥ 12 oportunidades
- Demostraciones de equipos Ricoh por mes: ≥ 6 demostraciones
- Tasa de conversión visita a oportunidad calificada: ≥ 25%
- Levantamientos de gestión documental completados por mes: ≥ 4 levantamientos

5. DOCUMENTOS Y SISTEMAS
- CRM corporativo Copikon (visitas, oportunidades, seguimiento)
- Formulario de levantamiento de necesidades de gestión documental
- Guía de argumentos de venta y manejo de objeciones
- Catálogo de equipos Ricoh y planes CPP vigentes
- Presentación corporativa Copikon para clientes industriales
- Equipo Ricoh de demostración regional
- Mapa de rutas y cobertura Aragua-Carabobo"""

MANUAL_VENDEDOR_LARA = """MANUAL DE PROCEDIMIENTO — Vendedor Renta Impresora y Gestión Documental (Lara, Portuguesa, Yaracuy)

1. OBJETIVO
Ejecutar la venta de campo, demostraciones de equipos Ricoh y levantamiento de necesidades de gestión documental en los estados Lara, Portuguesa y Yaracuy, generando oportunidades calificadas y apoyando el cierre de contratos en la región occidente de Copikon Venezuela.

2. ALCANCE
Aplica a todas las actividades de venta presencial en los estados Lara, Portuguesa y Yaracuy, con cobertura en los principales municipios: Barquisimeto, Cabudare, Acarigua, Guanare, San Felipe y zonas agroindustriales aledañas.

3. PROCEDIMIENTOS PRINCIPALES

3.1 Prospección y Planificación de Ruta en Región Occidente
- Planificar la ruta semanal considerando las distancias entre municipios de los tres estados (Lara, Portuguesa, Yaracuy).
- Realizar un mínimo de 4 visitas presenciales diarias dado el mayor tiempo de traslado intermunicipal de la región.
- Enfocar la prospección en el sector agroindustrial (Portuguesa), comercio minorista y mayorista (Barquisimeto) e instituciones públicas (alcaldías, hospitales, educación).
- Coordinar con el analista comercial regional la priorización semanal de prospectos y clientes a visitar.
- Registrar en el CRM el resultado de cada visita con fecha, contacto, interés detectado y próxima acción antes de las 6 pm del mismo día.

3.2 Demostraciones de Equipos Ricoh en la Región
- Coordinar el traslado del equipo de demostración al prospecto o realizar la demo en la sede de Copikon Barquisimeto.
- Adaptar el guion de demostración al perfil del cliente: para agroindustria destacar el escaneo de documentos de campo; para comercio, la velocidad y bajo costo por página.
- Mostrar las ventajas del mantenimiento preventivo incluido en el contrato de renta, especialmente relevante en zonas con menor disponibilidad de servicio técnico local.
- Demostrar la integración de los equipos Ricoh con el software de gestión documental de Copikon para digitalización de registros agropecuarios.
- Coordinar demostraciones grupales para empresas con múltiples sedes en la región cuando sea posible.

3.3 Levantamiento de Necesidades Documentales
- Aplicar el formulario de levantamiento de gestión documental con énfasis en empresas con grandes volúmenes de registros físicos: certificados fitosanitarios, guías de movilización, registros contables agrícolas.
- Identificar el nivel de digitalización actual del cliente y las herramientas que usa para el archivo de documentos.
- Documentar la urgencia o necesidad regulatoria que pueda acelerar la decisión (auditorías del SENIAT, inspecciones del SASA u otras entidades).
- Trasladar el formulario completo al analista regional para preparar la propuesta de servicio de gestión documental.
- Presentar testimonios o referencias de clientes similares en la región que ya usan los servicios de Copikon.

3.4 Cierre y Postventa en Región Occidente
- Apoyar al analista en la presentación de propuesta cuando se requiera presencia presencial por la distancia o preferencia del cliente.
- Gestionar objeciones típicas de la región (distancia del soporte técnico, conectividad, precio en mercado regional).
- Coordinar con logística el transporte del equipo Ricoh hasta la ubicación del cliente, incluyendo municipios rurales de Portuguesa y Yaracuy.
- Supervisar o ejecutar la instalación básica del equipo y la capacitación inicial al usuario final.
- Realizar visita de seguimiento post-instalación a los 15 y 30 días para verificar funcionamiento y detectar nuevas necesidades.

4. KPIs DEL CARGO
- Visitas de campo por semana en región occidente: ≥ 20 visitas
- Oportunidades calificadas generadas por mes: ≥ 10 oportunidades
- Demostraciones de equipos Ricoh por mes: ≥ 5 demostraciones
- Tasa de conversión visita a oportunidad calificada: ≥ 25%
- Levantamientos de gestión documental completados por mes: ≥ 4 levantamientos

5. DOCUMENTOS Y SISTEMAS
- CRM corporativo Copikon (visitas, oportunidades, seguimiento de campo)
- Formulario de levantamiento de necesidades de gestión documental
- Guía de argumentos de venta y manejo de objeciones (versión región occidente)
- Catálogo de equipos Ricoh y planes CPP vigentes
- Presentación corporativa Copikon adaptada al sector agroindustrial
- Equipo Ricoh de demostración asignado a la región
- Mapa de cobertura Lara-Portuguesa-Yaracuy con tiempos de traslado"""

# ─────────────────────────────────────────────────────────────────────────────
# FLUJOS (una sola línea de HTML)
# ─────────────────────────────────────────────────────────────────────────────

FLUJO_COORDINADOR = '<div class="flujo-section-title">Flujo de Gestión Comercial — Coordinador Comercial Renta Impresora y Gestión Documental</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Planificación Estratégica Mensual</div><div class="flujo-step-desc">Define metas de ventas nuevas, renovaciones y crecimiento de fleet por región; actualiza tarifario CPP con Ricoh Venezuela y distribuye objetivos a los tres analistas comerciales.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Coordinador Comercial</span><span class="flujo-badge entregable">Plan Comercial Mensual</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Revisión y Aprobación de Propuestas Regionales</div><div class="flujo-step-desc">Revisa las propuestas comerciales de los analistas que superen el 10% de descuento o condiciones especiales; aprueba o ajusta antes de enviar al cliente.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Coordinador Comercial</span><span class="flujo-badge entregable">Propuesta Aprobada</span><span class="flujo-badge decision">Aprobado / Ajuste Requerido</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Seguimiento Semanal del Pipeline</div><div class="flujo-step-desc">Realiza reunión de seguimiento con los tres analistas; revisa oportunidades en etapa de negociación avanzada y destraba cuellos de botella en aprobaciones o logística.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Coordinador Comercial</span><span class="flujo-badge entregable">Informe Pipeline Semanal</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Gestión del Contrato Marco Ricoh</div><div class="flujo-step-desc">Coordina con Ricoh Venezuela la disponibilidad de equipos, condiciones de garantía y SLA de mantenimiento; gestiona créditos y resolución de incidencias técnicas escaladas.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Coordinador Comercial</span><span class="flujo-badge entregable">Acta de Acuerdo con Ricoh</span><span class="flujo-badge sistema">Sistema Gestión Documental</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Control de Renovaciones y Alertas de Vencimiento</div><div class="flujo-step-desc">Monitorea el calendario de vencimientos; activa alertas a 90 días y coordina con analistas la estrategia de renovación o upselling para contratos próximos a vencer.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Coordinador Comercial</span><span class="flujo-badge entregable">Plan de Renovación por Región</span><span class="flujo-badge decision">Renovación / Upselling / No Renueva</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Informe Ejecutivo Mensual a Gerencia</div><div class="flujo-step-desc">Consolida resultados de las tres regiones (contratos nuevos, renovaciones, fleet instalado, ingresos CPP) y presenta informe ejecutivo con análisis de desviaciones y plan de acción.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Coordinador Comercial</span><span class="flujo-badge entregable">Informe Ejecutivo Mensual</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

FLUJO_ANALISTA_CARACAS = '<div class="flujo-section-title">Flujo Comercial — Analista Comercial Renta Impresora y Gestión Documental (Caracas)</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Ingreso y Calificación de Oportunidad</div><div class="flujo-step-desc">Recibe prospecto del vendedor de campo o fuente interna; califica la oportunidad según volumen de impresión estimado, segmento y urgencia; la registra en el CRM con etapa y valor estimado.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Caracas</span><span class="flujo-badge entregable">Oportunidad Calificada en CRM</span><span class="flujo-badge decision">Califica / No Califica</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Levantamiento y Análisis de Necesidades</div><div class="flujo-step-desc">Coordina con el vendedor la visita de levantamiento; analiza volumen de impresión, requerimientos de gestión documental y condiciones del cliente para estructurar la propuesta óptima.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Caracas</span><span class="flujo-badge entregable">Formulario de Levantamiento</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Elaboración y Envío de Propuesta Comercial</div><div class="flujo-step-desc">Prepara la propuesta CPP con modelo Ricoh adecuado, plan de páginas, suministros, SLA de mantenimiento y opciones de gestión documental; obtiene aprobación del coordinador si aplica y envía al cliente.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Caracas</span><span class="flujo-badge entregable">Propuesta Comercial Formal</span><span class="flujo-badge sistema">Plantilla CPP Corporativa</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Negociación y Cierre</div><div class="flujo-step-desc">Hace seguimiento activo a los 2, 5 y 10 días; atiende contrapropuestas del cliente; coordina ajustes de precio o condiciones con el coordinador; confirma aceptación del cliente.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Caracas</span><span class="flujo-badge entregable">Confirmación de Cierre</span><span class="flujo-badge decision">Acepta / Rechaza / Contraoferta</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Formalización del Contrato e Instalación</div><div class="flujo-step-desc">Coordina con administración la emisión del contrato de arrendamiento; gestiona firma por ambas partes; notifica al equipo técnico la fecha de instalación con mínimo 5 días hábiles de anticipación.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Caracas</span><span class="flujo-badge entregable">Contrato Firmado</span><span class="flujo-badge sistema">Sistema Gestión Documental</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Seguimiento Post-Instalación y Renovación</div><div class="flujo-step-desc">Realiza llamada de seguimiento a los 7 y 30 días; monitorea consumo mensual de páginas; activa gestión de renovación a los 60 días previos al vencimiento del contrato.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Caracas</span><span class="flujo-badge entregable">Informe de Satisfacción / Renovación</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

FLUJO_ANALISTA_ARAGUA = '<div class="flujo-section-title">Flujo Comercial — Analista Comercial Renta Impresora y Gestión Documental (Aragua, Carabobo)</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Prospección y Calificación Región Centro</div><div class="flujo-step-desc">Identifica prospectos en parques industriales y zonas comerciales de Aragua y Carabobo; califica según volumen de impresión y potencial documental; registra en el CRM con prioridad asignada.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Aragua-Carabobo</span><span class="flujo-badge entregable">Lista de Prospectos Calificados</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Levantamiento de Necesidades con Vendedor</div><div class="flujo-step-desc">Coordina con el vendedor regional la visita de levantamiento; analiza requerimientos de impresión industrial y necesidades de digitalización de documentos de manufactura o agroindustria.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Aragua-Carabobo</span><span class="flujo-badge entregable">Formulario de Levantamiento Completado</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Elaboración de Propuesta Adaptada al Perfil Industrial</div><div class="flujo-step-desc">Diseña la propuesta CPP con enfoque industrial; incluye opciones de gestión documental para procesos de manufactura (órdenes de producción, control de calidad); obtiene aprobación del coordinador si aplica.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Aragua-Carabobo</span><span class="flujo-badge entregable">Propuesta Comercial Industrial</span><span class="flujo-badge sistema">Plantilla CPP Corporativa</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Negociación y Cierre con Cliente Industrial</div><div class="flujo-step-desc">Presenta la propuesta con el vendedor cuando se requiera; hace seguimiento estructurado; gestiona objeciones de precio y logística con argumentos de costo-beneficio industrial.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Aragua-Carabobo</span><span class="flujo-badge entregable">Acuerdo de Cierre</span><span class="flujo-badge decision">Acepta / Negocia / Declina</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Formalización y Coordinación de Instalación</div><div class="flujo-step-desc">Gestiona la emisión y firma del contrato; coordina con logística el transporte del equipo Ricoh hasta la planta o sede del cliente; confirma condiciones de instalación (red, espacio, electricidad).</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Aragua-Carabobo</span><span class="flujo-badge entregable">Contrato Firmado y Equipo Instalado</span><span class="flujo-badge sistema">Sistema Gestión Documental</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Monitoreo de Cartera y Renovaciones</div><div class="flujo-step-desc">Revisa mensualmente el consumo de páginas de clientes activos; gestiona ajustes de plan CPP cuando hay desviaciones; activa proceso de renovación a los 60 días del vencimiento.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Aragua-Carabobo</span><span class="flujo-badge entregable">Reporte Mensual de Cartera</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

FLUJO_ANALISTA_LARA = '<div class="flujo-section-title">Flujo Comercial — Analista Comercial Renta Impresora y Gestión Documental (Lara, Portuguesa, Yaracuy)</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Prospección Región Occidente</div><div class="flujo-step-desc">Identifica prospectos en sectores agroindustrial (Portuguesa), comercio (Barquisimeto) e institucional (Yaracuy, Lara); ingresa al CRM con segmento, municipio y prioridad estimada.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Mapa de Prospectos Región Occidente</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Levantamiento con Consideraciones Logísticas Regionales</div><div class="flujo-step-desc">Coordina con el vendedor la visita de levantamiento incluyendo evaluación de conectividad y distancia al soporte técnico; documenta requerimientos especiales del entorno agroindustrial.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Formulario de Levantamiento Regional</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Elaboración de Propuesta con SLA Adaptado</div><div class="flujo-step-desc">Diseña la propuesta CPP ajustando el SLA de mantenimiento a los tiempos de traslado de la región; incluye opciones de gestión documental para digitalización de registros agropecuarios y fitosanitarios.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Propuesta CPP con SLA Regional</span><span class="flujo-badge sistema">Plantilla CPP Corporativa</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Negociación y Cierre en Mercado Regional</div><div class="flujo-step-desc">Gestiona la negociación destacando la continuidad operativa y el soporte incluido; maneja objeciones de distancia y precio; coordina con coordinador los ajustes necesarios para cerrar.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Acuerdo Comercial</span><span class="flujo-badge decision">Cierra / Negocia / No Cierra</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Formalización y Logística de Instalación Remota</div><div class="flujo-step-desc">Coordina la firma del contrato y la logística especial de transporte del equipo Ricoh a municipios rurales; verifica condiciones de instalación remota y acompaña el proceso con el vendedor.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Contrato Firmado / Acta de Instalación</span><span class="flujo-badge sistema">Sistema Gestión Documental</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Seguimiento de Cartera y Retención Occidente</div><div class="flujo-step-desc">Monitorea consumo mensual de páginas y propone ajustes de plan; gestiona reclamos coordinando soporte técnico regional; activa renovación a los 60 días previos al vencimiento con estrategia de retención.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Analista Comercial Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Reporte de Retención y Renovación</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

FLUJO_VENDEDOR_CARACAS = '<div class="flujo-section-title">Flujo de Venta de Campo — Vendedor Renta Impresora y Gestión Documental (Caracas)</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Planificación de Ruta y Agenda de Visitas</div><div class="flujo-step-desc">Define con el analista comercial la ruta diaria de visitas en Caracas; prioriza prospectos por etapa del pipeline y potencial; carga la agenda en el CRM móvil antes de iniciar la jornada.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Caracas</span><span class="flujo-badge entregable">Ruta Diaria Planificada</span><span class="flujo-badge sistema">CRM Copikon (móvil)</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Visita de Prospección y Contacto con Decisor</div><div class="flujo-step-desc">Realiza la visita presencial; identifica al decisor de compra (gerente administrativo, director de operaciones); presenta brevemente los servicios de renta Ricoh y gestión documental de Copikon.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Caracas</span><span class="flujo-badge entregable">Datos de Contacto del Decisor</span><span class="flujo-badge decision">Interesado / No Interesado / Próxima Cita</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Demostración de Equipo Ricoh y Levantamiento</div><div class="flujo-step-desc">Ejecuta la demostración del equipo Ricoh mostrando impresión, copiado, escaneo y gestión documental; aplica el formulario de levantamiento de necesidades documentales para clientes con alto volumen de papel.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Caracas</span><span class="flujo-badge entregable">Demo Realizada / Formulario Completado</span><span class="flujo-badge sistema">Equipo Ricoh Demo</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Traslado de Información al Analista Comercial</div><div class="flujo-step-desc">Envía el formulario de levantamiento y las notas de la visita al analista comercial; actualiza el CRM con el resultado de la demo, interés del cliente y datos para la propuesta.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Caracas</span><span class="flujo-badge entregable">Oportunidad Actualizada en CRM</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Apoyo al Cierre y Gestión de Objeciones</div><div class="flujo-step-desc">Acompaña al analista en la reunión de presentación de propuesta; gestiona objeciones de precio, duración y marca usando los argumentos de venta corporativos; detecta y comunica señales de cierre al analista.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Caracas</span><span class="flujo-badge entregable">Reporte de Objeciones y Señales de Cierre</span><span class="flujo-badge decision">Cierra / Requiere Ajuste / Perdido</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Instalación y Seguimiento Postventa</div><div class="flujo-step-desc">Está presente en la instalación del equipo Ricoh para reforzar la relación con el usuario final; realiza visita de seguimiento a los 30 días para verificar satisfacción y detectar oportunidades de upselling.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Caracas</span><span class="flujo-badge entregable">Acta de Instalación / Informe Postventa</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

FLUJO_VENDEDOR_ARAGUA = '<div class="flujo-section-title">Flujo de Venta de Campo — Vendedor Renta Impresora y Gestión Documental (Aragua, Carabobo)</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Planificación de Ruta en Parques Industriales</div><div class="flujo-step-desc">Coordina con el analista comercial la ruta semanal priorizando parques industriales de Valencia y Maracay; carga la agenda en el CRM y prepara el material de prospección según el perfil industrial de cada zona.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Aragua-Carabobo</span><span class="flujo-badge entregable">Ruta Semanal Industrial</span><span class="flujo-badge sistema">CRM Copikon (móvil)</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Visita y Contacto con Decisor Industrial</div><div class="flujo-step-desc">Realiza la visita presencial en la planta o sede administrativa; identifica al gerente de compras, director de operaciones o administrador; presenta los beneficios de la renta Ricoh para entornos de alta productividad.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Aragua-Carabobo</span><span class="flujo-badge entregable">Contacto Decisor Registrado</span><span class="flujo-badge decision">Interesado / Cita Demo / No Interesado</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Demostración Técnica y Levantamiento Documental Industrial</div><div class="flujo-step-desc">Ejecuta la demo del equipo Ricoh enfocada en escaneo masivo, impresión de alto volumen y conectividad en red; aplica el formulario de levantamiento documental para manufactura (órdenes de producción, control de calidad, RRHH).</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Aragua-Carabobo</span><span class="flujo-badge entregable">Demo Realizada / Levantamiento Industrial</span><span class="flujo-badge sistema">Equipo Ricoh Demo Regional</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Registro y Traslado al Analista</div><div class="flujo-step-desc">Actualiza el CRM con resultado de la visita, datos del cliente, volumen estimado de impresión y necesidades documentales identificadas; envía el formulario de levantamiento al analista comercial regional.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Aragua-Carabobo</span><span class="flujo-badge entregable">Oportunidad Registrada en CRM</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Apoyo al Cierre y Coordinación de Instalación</div><div class="flujo-step-desc">Apoya al analista en la presentación de propuesta; gestiona objeciones específicas del entorno industrial (costo de mantenimiento, SLA); coordina con logística la fecha y condiciones de instalación en planta.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Aragua-Carabobo</span><span class="flujo-badge entregable">Confirmación de Instalación</span><span class="flujo-badge decision">Contrato Firmado / En Proceso / Perdido</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Instalación y Visitas de Seguimiento Postventa</div><div class="flujo-step-desc">Supervisa la instalación en la planta y capacita al usuario final; realiza visitas de seguimiento a los 15 y 30 días post-instalación; reporta al analista cualquier necesidad adicional o insatisfacción detectada.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Aragua-Carabobo</span><span class="flujo-badge entregable">Acta de Instalación / Informe Postventa</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

FLUJO_VENDEDOR_LARA = '<div class="flujo-section-title">Flujo de Venta de Campo — Vendedor Renta Impresora y Gestión Documental (Lara, Portuguesa, Yaracuy)</div><div class="flujo-step"><div class="flujo-step-num">1</div><div class="flujo-step-body"><div class="flujo-step-title">Planificación de Ruta Intermunicipal</div><div class="flujo-step-desc">Planifica la ruta semanal optimizando los traslados entre Barquisimeto, Acarigua, Guanare y San Felipe; coordina con el analista la priorización de visitas y carga la agenda en el CRM antes de partir.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Ruta Intermunicipal Planificada</span><span class="flujo-badge sistema">CRM Copikon (móvil)</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">2</div><div class="flujo-step-body"><div class="flujo-step-title">Visita al Cliente Agroindustrial o Comercial</div><div class="flujo-step-desc">Realiza la visita presencial adaptando el discurso al sector del cliente (agroindustria en Portuguesa, comercio en Barquisimeto, institucional en Yaracuy); identifica al decisor y detecta la necesidad principal.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Contacto Decisor / Necesidad Identificada</span><span class="flujo-badge decision">Interesado / Cita Demo / No Interesado</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">3</div><div class="flujo-step-body"><div class="flujo-step-title">Demostración Ricoh y Levantamiento Documental Agroindustrial</div><div class="flujo-step-desc">Ejecuta la demo del equipo Ricoh destacando el escaneo de documentos de campo y la integración con gestión documental; aplica el formulario de levantamiento para identificar volúmenes de certificados, guías y registros agropecuarios.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Demo / Formulario de Levantamiento</span><span class="flujo-badge sistema">Equipo Ricoh Demo Occidente</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">4</div><div class="flujo-step-body"><div class="flujo-step-title">Registro en CRM y Traslado al Analista</div><div class="flujo-step-desc">Actualiza el CRM con resultado de visita, datos del cliente y necesidades documentales específicas; envía el formulario al analista regional para elaborar la propuesta con SLA adaptado a la distancia.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Oportunidad Registrada en CRM</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">5</div><div class="flujo-step-body"><div class="flujo-step-title">Apoyo al Cierre y Logística Remota</div><div class="flujo-step-desc">Acompaña al analista en la presentación de propuesta presencial o virtual; gestiona objeciones de distancia al soporte técnico y precio; coordina con logística el transporte del equipo a municipios rurales.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Plan de Instalación Remota</span><span class="flujo-badge decision">Contrato Firmado / En Proceso / Perdido</span></div></div></div><div class="flujo-arrow">↓</div><div class="flujo-step"><div class="flujo-step-num">6</div><div class="flujo-step-body"><div class="flujo-step-title">Instalación, Capacitación y Seguimiento Postventa</div><div class="flujo-step-desc">Ejecuta o supervisa la instalación básica del equipo y capacita al usuario final en el sitio; realiza visita de seguimiento a los 15 y 30 días; reporta al analista cualquier necesidad de soporte técnico o ampliación del servicio.</div><div style="margin-top:5px;"><span class="flujo-badge responsable">Vendedor Lara-Portuguesa-Yaracuy</span><span class="flujo-badge entregable">Acta de Instalación / Reporte Postventa</span><span class="flujo-badge sistema">CRM Copikon</span></div></div></div>'

# ─────────────────────────────────────────────────────────────────────────────
# ASSEMBLER
# ─────────────────────────────────────────────────────────────────────────────

data = {
    "coordinador-comercial-renta-impresora-gestion-documental": {
        "manual": MANUAL_COORDINADOR,
        "flujo": FLUJO_COORDINADOR
    },
    "analista-comercial-renta-impresora-gestion-documento-caracas": {
        "manual": MANUAL_ANALISTA_CARACAS,
        "flujo": FLUJO_ANALISTA_CARACAS
    },
    "analista-comercial-renta-impresora-gestion-documento-aragua-carabobo": {
        "manual": MANUAL_ANALISTA_ARAGUA_CARABOBO,
        "flujo": FLUJO_ANALISTA_ARAGUA
    },
    "analista-comercial-renta-impresora-gestion-documento-lara-portuguesa-yaracuy": {
        "manual": MANUAL_ANALISTA_LARA,
        "flujo": FLUJO_ANALISTA_LARA
    },
    "vendedor-renta-impresora-gestion-documentos-caracas": {
        "manual": MANUAL_VENDEDOR_CARACAS,
        "flujo": FLUJO_VENDEDOR_CARACAS
    },
    "vendedor-renta-impresora-gestion-documento-aragua-carabobo": {
        "manual": MANUAL_VENDEDOR_ARAGUA_CARABOBO,
        "flujo": FLUJO_VENDEDOR_ARAGUA
    },
    "vendedor-renta-impresora-gestion-documento-lara-portuguesa-yaracuy": {
        "manual": MANUAL_VENDEDOR_LARA,
        "flujo": FLUJO_VENDEDOR_LARA
    }
}

out_path = "/home/user/workspace/copikon-organigrama-v2/manuales_flujos_renta_impresora.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Saved to {out_path}")
print(f"Keys: {list(data.keys())}")
