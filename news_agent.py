# ---------------------------------------------------------------------------
# Eventos hardcodeados con juicios pre-computados por Claude Sonnet 4.6.
# En producción, estos serían generados en tiempo real via web search + LLM.
# ---------------------------------------------------------------------------
EVENTS = [
    {
        "descripcion": "Recital de Coldplay en el Estadio Monumental",
        "fecha": "2024-11-20",
        "lineas_afectadas": ["LineaD"],
        "estaciones_afectadas": ["Congreso de Tucuman", "Juramento", "Jose Hernandez"],
        "ventana_inicio": "21:30",
        "ventana_fin": "23:59",
        "factor": 2.2,
        "tipo": "aumento",
        "judgment": (
            "La predicción base de {base} pasajeros no contempla el recital de Coldplay "
            "en el Estadio Monumental (~65.000 personas). Eventos de esta escala generan "
            "picos de demanda concentrados en la franja de salida: la mayoría del público "
            "llega en auto o remís pero regresa en subte, saturando las estaciones del "
            "extremo norte de LineaD. Aplico un factor 2.2x y ajusto a {adjusted} pasajeros. "
            "Recomiendo anticipar demoras y considerar frecuencia reforzada."
        ),
    },
    {
        "descripcion": "Corte total de servicio en LineaC por mantenimiento de vías",
        "fecha": "2024-11-18",
        "lineas_afectadas": ["LineaC"],
        "estaciones_afectadas": [
            "Constitucion", "San Juan", "Independencia", "Mariano Moreno",
            "Avenida de Mayo", "Diagonal Norte", "Lavalle",
            "General San Martin", "Retiro",
        ],
        "ventana_inicio": "00:00",
        "ventana_fin": "23:59",
        "factor": 0.1,
        "tipo": "disminucion",
        "judgment": (
            "El corte total de LineaC elimina prácticamente toda la demanda orgánica "
            "en sus estaciones. La predicción base de {base} pasajeros refleja un día "
            "normal de operación, lo cual es incorrecto. Una fracción menor del flujo "
            "habitual puede aparecer como transbordos en Diagonal Norte o Independencia "
            "desde otras líneas, pero el volumen neto cae drásticamente. "
            "Corrijo a {adjusted} pasajeros, asumiendo tráfico residual de orientación."
        ),
    },
    {
        "descripcion": "Marcha sindical con concentración en Plaza de Mayo",
        "fecha": "2024-11-22",
        "lineas_afectadas": ["LineaA", "LineaC", "LineaD", "LineaE"],
        "estaciones_afectadas": [
            "Plaza de Mayo", "Peru", "Piedras",
            "Avenida de Mayo", "Diagonal Norte",
            "Catedral", "9 de julio",
            "Bolivar",
        ],
        "ventana_inicio": "15:00",
        "ventana_fin": "19:00",
        "factor": 1.5,
        "tipo": "aumento",
        "judgment": (
            "Las marchas con concentración en Plaza de Mayo incrementan la demanda "
            "en las estaciones céntricas de múltiples líneas, tanto en el flujo de "
            "llegada (13:00-16:00) como de dispersión (17:00-19:30). La predicción "
            "base de {base} pasajeros no captura este efecto porque el patrón no "
            "está representado de forma consistente en los datos de entrenamiento. "
            "Aplico 1.5x considerando que parte del público usa otras vías de acceso. "
            "Estimación ajustada: {adjusted} pasajeros."
        ),
    },
]


def fetch_events() -> dict:
    """Devuelve los eventos activos hardcodeados."""
    return {"events": EVENTS}


def get_judgment(event: dict, base: float, adjusted: float) -> str:
    """Devuelve el juicio pre-computado con los números reales interpolados."""
    return event["judgment"].format(
        base=round(base),
        adjusted=round(adjusted),
    )
