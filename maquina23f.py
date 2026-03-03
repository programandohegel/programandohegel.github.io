#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MÁQUINA HEGELIANA – SISTEMA COMPLETO (Capítulos I, II y III)
Basado en la edición de W. Roces (FCE)

VERSIÓN INTEGRAL CON LOS TRES PRIMEROS CAPÍTULOS DE LA FENOMENOLOGÍA
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any, TypedDict, Union
from enum import Enum
from datetime import datetime
import re
from pathlib import Path

# -------------------------------------------------------------------
# GLOSARIO BILINGÜE
# -------------------------------------------------------------------
GLOSARIO = {
    "Aufhebung": "superación (conservar-negar-trascender)",
    "Ding": "cosa",
    "Eigenschaften": "propiedades",
    "Eins": "uno",
    "Auch": "también",
    "Verstand": "entendimiento",
    "Kraft": "fuerza",
    "Äußerung": "expresión",
    "Gesetz": "ley",
    "Erscheinung": "fenómeno",
    "übersinnliche Welt": "mundo suprasensible",
    "verkehrte Welt": "mundo invertido",
    "Unendlichkeit": "infinitud",
    "für uns": "para nosotros",
    "für es": "para la conciencia"
}

def t(termino_aleman: str) -> str:
    """Devuelve el término en español según el glosario."""
    return GLOSARIO.get(termino_aleman, termino_aleman)


# -------------------------------------------------------------------
# TYPED DICTS (definiciones necesarias)
# -------------------------------------------------------------------
class ContradiccionDict(TypedDict):
    id: str
    tipo: str
    descripcion: str
    detalle: Dict[str, str]

class PatronDialecticoDict(TypedDict):
    nombre: str
    descripcion: str
    ejemplos: List[str]
    aplicacion_futura: str
    fuente_capitulo: str

class TransicionDict(TypedDict):
    desde: str
    hacia: str
    razon: str
    timestamp: str


# -------------------------------------------------------------------
# ENUMS Y ESTRUCTURAS BASE
# -------------------------------------------------------------------
class EtapaFenomenologica(Enum):
    CONCIENCIA = "Conciencia"
    AUTOCONCIENCIA = "Autoconciencia"
    RAZON = "Razon"
    ESPIRITU = "Espíritu"
    RELIGION = "Religión"
    SABER_ABSOLUTO = "Saber Absoluto"

class FiguraConciencia(Enum):
    CONCIENCIA_SENSIBLE = "Conciencia sensible"
    PERCEPCION = "Percepción"
    ENTENDIMIENTO = "Entendimiento"
    FUERZA = "Fuerza y juego de fuerzas"
    MUNDO_SUPRASENSIBLE = "Mundo suprasensible"
    LEY = "Ley"
    MUNDO_INVERTIDO = "Mundo invertido"
    INFINITUD = "Infinitud"
    AUTOCONCIENCIA = "Autoconciencia"
    RAZON = "Razón"


@dataclass
class FiguraPhenomenologica:
    id: str
    nombre: str
    tipo_figura: FiguraConciencia
    etapa: EtapaFenomenologica
    texto_original: str = ""
    experiencia_conciencia: str = ""
    verdad_aparece: str = ""
    verdad_real: str = ""
    contradiccion_interna: str = ""
    superacion_hacia: List[str] = field(default_factory=list)
    leccion_dialectica: str = ""
    referencias: Dict[str, str] = field(default_factory=dict)
    metáforas_clave: List[str] = field(default_factory=list)
    notas_analisis: List[str] = field(default_factory=list)
    perspectiva: str = "para nosotros"
    
    # CAMPOS AMPLIADOS PARA ANÁLISIS DETALLADO
    ejemplos_concretos: List[Dict[str, str]] = field(default_factory=list)
    momentos_dialecticos: List[str] = field(default_factory=list)
    ironia_linguistica: str = ""
    perspectiva_dual: Dict[str, str] = field(default_factory=dict)

    def to_dict(self):
        d = asdict(self)
        d["tipo_figura"] = self.tipo_figura.value
        d["etapa"] = self.etapa.value
        d["timestamp"] = datetime.now().isoformat()
        return d


# -------------------------------------------------------------------
# MEMORIA DIALÉCTICA (CAPÍTULOS I, II Y III)
# -------------------------------------------------------------------
class MemoriaDialectica:
    """Almacena patrones y lecciones extraídas de figuras ya analizadas."""

    def __init__(self):
        self.memoria = {
            'patrones_detectados': [],
            'errores_evitables': [],
            'reglas_inferenciales': [],
            'lecciones': {},
            'lecciones_entendimiento': {},
            'violaciones_reglas': []
        }
        self._inicializar_desde_capitulos()

    def _inicializar_desde_capitulos(self):
        """Carga las lecciones de los capítulos I, II y III."""

        # Capítulo I - Certeza sensible
        self.memoria['lecciones']['certeza_sensible'] = {
            'leccion_1': 'Todo intento de fijar lo singular produce universalización.',
            'leccion_2': 'La mediación es inevitable incluso en la "inmediatez".',
            'leccion_3': 'La verdad sensible depende del contexto que la niega.',
            'leccion_4': 'El lenguaje expresa lo contrario de lo que la conciencia pretende.',
            'leccion_5': 'La verdad está en el movimiento, no en puntos fijos.',
            'leccion_6': 'El lenguaje es testigo de la verdad contra la conciencia.',
            'leccion_7': 'La experiencia es el movimiento mismo, no un resultado.',
            'leccion_8': 'El "esto" se despliega en tres momentos: ahora, aquí, yo.',
            'leccion_9': 'La negación es determinada: el ahora NO es noche (pero podría ser día).',
            'leccion_10': 'La verdad de la CS es su propio fracaso mostrado.'
        }

        # Capítulo II - Percepción
        self.memoria['lecciones']['percepcion'] = {
            'leccion_p1': 'La cosa se presenta como unidad de múltiples propiedades, pero esta unidad es problemática.',
            'leccion_p2': 'El "también" y el "uno" son momentos contrapuestos.',
            'leccion_p3': 'La conciencia oscila entre atribuir la unidad al objeto o a sí misma.',
            'leccion_p4': 'El "en tanto que" es un recurso sofístico.',
            'leccion_p5': 'La cosa se disuelve en materias independientes o en abstracciones.',
            'leccion_p6': 'El ser para sí implica ya ser para otro.',
            'leccion_p7': 'La universalidad incondicionada es el resultado necesario.',
            'leccion_p8': 'La propiedad esencial lleva a la relación con lo otro y la cosa se derrumba.',
            'leccion_p9': 'La percepción es un juego de abstracciones vacías (singularidad/universalidad).',
            'leccion_p10': 'El entendimiento percipiente (buen sentido) es presa de estas abstracciones.',
            'leccion_p11': 'La verdad de la percepción es su propia superación hacia el entendimiento.'
        }

        # Capítulo III - Entendimiento
        self.memoria['lecciones_entendimiento'] = {
            'leccion_e1': 'El entendimiento contempla lo verdadero sin saberse en él.',
            'leccion_e2': 'La fuerza es unidad de ser en sí y ser para otro.',
            'leccion_e3': 'La fuerza solo es en su exteriorización.',
            'leccion_e4': 'El juego de fuerzas es la realización de la fuerza como dualidad.',
            'leccion_e5': 'Cada fuerza es solo por la otra; la independencia es ilusoria.',
            'leccion_e6': 'La realidad de la fuerza es su desaparecer.',
            'leccion_e7': 'El mundo suprasensible es el concepto como concepto.',
            'leccion_e8': 'El mundo invertido es la ley de la pura diferencia.',
            'leccion_e9': 'La infinitud es la negación de la negación.',
            'leccion_e10': 'La infinitud es el concepto de la autoconciencia.',
            'leccion_e11': 'La ley es la imagen constante del fenómeno, pero tautológica.',
            'leccion_e12': 'El mundo suprasensible es el fenómeno en cuanto fenómeno, no otro mundo.',
            'leccion_e13': 'La diferencia en sí misma es la esencia del mundo suprasensible.',
            'leccion_e14': 'La explicación tautológica revela el cambio absoluto en lo interior.',
            'leccion_e15': 'El mundo invertido muestra que lo opuesto es lo mismo.',
            'leccion_e16': 'La infinitud es la unidad de los opuestos y el concepto de la autoconciencia.'
        }

        # Reglas inferenciales (todos los capítulos)
        self.memoria['reglas_inferenciales'] = [
            "REGLA 1: Todo intento de fijar lo singular produce universalización.",
            "REGLA 2: La mediación es inevitable incluso en la 'inmediatez'.",
            "REGLA 3: La verdad sensible depende del contexto que la niega.",
            "REGLA 4: La negación no es aniquilación, sino superación conservante (Aufhebung).",
            "REGLA 5: La cosa (Ding) es una unidad contradictoria de uno y también.",
            "REGLA 6: El 'en tanto que' es un recurso sofístico que escinde la unidad.",
            "REGLA 7: El ser para sí implica ser para otro; la independencia es autocontradictoria.",
            "REGLA 8: La propiedad esencial de una cosa la lleva necesariamente a la relación con otras.",
            "REGLA 9: La percepción oscila entre atribuir la unidad al objeto o al sujeto.",
            "REGLA 10: La universalidad incondicionada surge del fracaso de la percepción.",
            "REGLA 11: La fuerza (Kraft) se manifiesta necesariamente en su expresión.",
            "REGLA 12: El juego de fuerzas es la mutua solicitación; cada fuerza es por la otra.",
            "REGLA 13: La ley (Gesetz) es el concepto estable del fenómeno, pero tautológico.",
            "REGLA 14: El mundo suprasensible es la verdad del fenómeno, pero vacío.",
            "REGLA 15: El mundo invertido (verkehrte Welt) es el reverso necesario del primero.",
            "REGLA 16: La infinitud (Unendlichkeit) es la negación de la negación, el retorno a sí.",
            "REGLA 17: La explicación científica es un movimiento tautológico que no añade contenido.",
            "REGLA 18: La diferencia interna es la esencia de la infinitud.",
        ]

        # Patrones dialécticos detectados (todos los capítulos)
        self.memoria['patrones_detectados'] = [
            {
                'nombre': 'Patrón de Universalización',
                'descripcion': 'Todo intento de fijar lo singular produce universalización.',
                'ejemplos': ['Ahora → ahora universal', 'Aquí → aquí universal'],
                'aplicacion_futura': 'Predecir que la Percepción intentará estabilizar singularidades.',
                'fuente_capitulo': 'Certeza sensible'
            },
            {
                'nombre': 'Patrón de Mediación Ocultada',
                'descripcion': 'Lo que se presenta como inmediato siempre revela mediación.',
                'ejemplos': ['El ahora mediado por negación (no es noche, no es día)'],
                'aplicacion_futura': 'Buscar mediaciones ocultas en la Percepción.',
                'fuente_capitulo': 'Certeza sensible'
            },
            {
                'nombre': 'Patrón de Oscilación Unidad-Multiplicidad',
                'descripcion': 'La conciencia no puede mantener simultáneamente la unidad y la multiplicidad.',
                'ejemplos': ['La cosa es una y también múltiple', 'La sal es blanca y también salina'],
                'aplicacion_futura': 'En el Entendimiento, buscar la unidad en leyes universales.',
                'fuente_capitulo': 'Percepción'
            },
            {
                'nombre': 'Patrón del "También" y el "Uno"',
                'descripcion': 'La cosa se presenta como también (multiplicidad indiferente) y como uno (unidad excluyente).',
                'ejemplos': ['La sal: blanca, salina, cúbica (también) / una cosa (uno)'],
                'aplicacion_futura': 'El entendimiento buscará la unidad de estas determinaciones en la fuerza.',
                'fuente_capitulo': 'Percepción'
            },
            {
                'nombre': 'Patrón de la Propiedad Esencial',
                'descripcion': 'La propiedad esencial, que debía garantizar la independencia, lleva a la relación con lo otro.',
                'ejemplos': ['La sal es salina solo en oposición a lo dulce'],
                'aplicacion_futura': 'En el entendimiento, la fuerza se manifiesta en su expresión (oposición).',
                'fuente_capitulo': 'Percepción'
            },
            {
                'nombre': 'Patrón de la Universalidad Afectada de Contraposición',
                'descripcion': 'El universal que emerge de la percepción contiene en sí la diferencia.',
                'ejemplos': ['Universal que se separa en extremos (singular/universal, uno/también)'],
                'aplicacion_futura': 'Tránsito al entendimiento.',
                'fuente_capitulo': 'Percepción'
            },
            {
                'nombre': 'Patrón de la Fuerza',
                'descripcion': 'La fuerza es la unidad de ser en sí y ser para otro; solo es en su exteriorización.',
                'ejemplos': ['Fuerza magnética que solo se manifiesta en la interacción'],
                'aplicacion_futura': 'El juego de fuerzas lleva a la ley.',
                'fuente_capitulo': 'Entendimiento'
            },
            {
                'nombre': 'Patrón de Tautología Legal',
                'descripcion': 'La ley universal del fenómeno no añade contenido nuevo.',
                'ejemplos': ['Atracción universal: todo es diferente de lo otro'],
                'aplicacion_futura': 'La conciencia descubrirá que la legalidad es su propia actividad.',
                'fuente_capitulo': 'Entendimiento'
            },
            {
                'nombre': 'Patrón de Inversión',
                'descripcion': 'El mundo suprasensible se determina como el inverso del mundo fenoménico.',
                'ejemplos': ['El castigo que en el fenómeno es infamia, en el mundo invertido es gracia'],
                'aplicacion_futura': 'La autoconciencia emergerá como la unidad de los opuestos.',
                'fuente_capitulo': 'Entendimiento (mundo invertido)'
            },
            {
                'nombre': 'Patrón de Infinitud',
                'descripcion': 'La negación de la negación conduce al retorno a sí mismo.',
                'ejemplos': ['El mundo invertido se sobrepasa a sí mismo y retorna a la unidad'],
                'aplicacion_futura': 'Tránsito a la autoconciencia.',
                'fuente_capitulo': 'Entendimiento (infinitud)'
            },
            {
                'nombre': 'Patrón de la Explicación Tautológica',
                'descripcion': 'La explicación científica repite lo mismo en diferentes palabras.',
                'ejemplos': ['Reducir la ley de la electricidad a la fuerza eléctrica'],
                'aplicacion_futura': 'La conciencia se encuentra a sí misma en este movimiento.',
                'fuente_capitulo': 'Entendimiento'
            }
        ]


# -------------------------------------------------------------------
# MOTOR DE REGLAS DIALÉCTICAS
# -------------------------------------------------------------------
class RuleEngine:
    """Motor que verifica reglas dialécticas contra fragmentos."""

    def __init__(self, memoria: MemoriaDialectica):
        self.memoria = memoria
        self.reglas_activas = self._cargar_reglas()
        self.violaciones = []

    def _cargar_reglas(self) -> List[Dict]:
        """Convierte las reglas inferenciales en objetos ejecutables."""
        reglas = []
        for r in self.memoria.memoria.get('reglas_inferenciales', []):
            reglas.append({'texto': r, 'activa': True})
        return reglas

    def verificar_fragmento(self, fragmento: str, contexto: Dict) -> List[Dict]:
        """Evalúa qué reglas se aplican en el fragmento."""
        resultados = []
        fragmento_lower = fragmento.lower()
        for regla in self.reglas_activas:
            texto_regla = regla['texto'].lower()
            aplicada = False
            evidencia = ""

            # Reglas de la certeza sensible
            if 'universalización' in texto_regla and ('esto' in fragmento_lower or 'singular' in fragmento_lower):
                aplicada = True
                evidencia = "Mención de singularidad/universalización"
            
            # Reglas de la percepción
            elif 'uno y también' in texto_regla and ('también' in fragmento_lower or 'uno' in fragmento_lower):
                aplicada = True
                evidencia = "Referencia a la unidad/multiplicidad de la cosa"
            elif 'en tanto que' in texto_regla and ('en tanto que' in fragmento_lower):
                aplicada = True
                evidencia = "Uso del recurso sofístico 'en tanto que'"
            elif 'ser para sí' in texto_regla and ('ser para sí' in fragmento_lower or 'para sí' in fragmento_lower):
                aplicada = True
                evidencia = "Concepto de ser para sí"
            elif 'propiedad esencial' in texto_regla and ('propiedad esencial' in fragmento_lower or 'determinabilidad esencial' in fragmento_lower):
                aplicada = True
                evidencia = "Referencia a propiedad esencial"
            
            # Reglas del entendimiento
            elif 'fuerza' in texto_regla and ('fuerza' in fragmento_lower or 'exteriorización' in fragmento_lower or 'juego de fuerzas' in fragmento_lower):
                aplicada = True
                evidencia = "Concepto de fuerza/expresión"
            elif 'ley' in texto_regla and ('ley' in fragmento_lower or 'atracción universal' in fragmento_lower or 'tautología' in fragmento_lower):
                aplicada = True
                evidencia = "Referencia a ley o atracción universal"
            elif 'mundo suprasensible' in texto_regla and ('mundo suprasensible' in fragmento_lower or 'interior' in fragmento_lower or 'más allá' in fragmento_lower):
                aplicada = True
                evidencia = "Referencia al mundo suprasensible"
            elif 'mundo invertido' in texto_regla and ('invertido' in fragmento_lower or 'contrario' in fragmento_lower or 'inversión' in fragmento_lower):
                aplicada = True
                evidencia = "Referencia a inversión"
            elif 'infinitud' in texto_regla and ('infinitud' in fragmento_lower or 'negación de la negación' in fragmento_lower or 'retorno a sí' in fragmento_lower):
                aplicada = True
                evidencia = "Concepto de infinitud"
            elif 'explicación' in texto_regla and ('explicación' in fragmento_lower or 'tautología' in fragmento_lower):
                aplicada = True
                evidencia = "Referencia a explicación tautológica"

            if aplicada:
                resultados.append({
                    'regla': regla['texto'],
                    'aplicada': True,
                    'evidencia': evidencia,
                    'fragmento': fragmento[:50] + "..."
                })
        return resultados

    def registrar_violacion(self, violacion: Dict):
        self.violaciones.append(violacion)
        self.memoria.memoria.setdefault('violaciones_reglas', []).append(violacion)


# -------------------------------------------------------------------
# ANÁLISIS CORRELATIVO
# -------------------------------------------------------------------
class AnalisisCorrelativo:
    """
    Procesa fragmentos de texto de forma correlativa:
    - Conecta cada nuevo fragmento con el anterior.
    - Extrae conceptos y movimientos dialécticos.
    - Detecta transiciones.
    """

    def __init__(self, memoria: Optional[MemoriaDialectica] = None):
        self.linea_dialectica = []
        self.conceptos_activos = set()
        self.ultimo_contexto = None
        self.memoria = memoria if memoria else MemoriaDialectica()
        self.estado_actual = "Certeza sensible"
        self.perspectiva = "para nosotros"
        self.rule_engine = RuleEngine(self.memoria) if memoria else None

    def cambiar_perspectiva(self, perspectiva: str):
        if perspectiva in ["para nosotros", "para la conciencia", "für uns", "für es"]:
            self.perspectiva = perspectiva

    def establecer_conexion(self, contenido: str, contexto_previo: Optional[Dict]) -> str:
        if not contexto_previo:
            return "INICIO: Primer fragmento del capítulo."
        conectores = []
        for palabra in ['por tanto', 'ahora', 'sin embargo', 'así', 'pero', 'continuación', 'de hecho']:
            if palabra in contenido.lower():
                conectores.append(f"conecta mediante '{palabra}'")
        return f"Continúa desde {contexto_previo.get('ultimo_tema','...')}. " + "; ".join(conectores)

    def extraer_elementos(self, contenido: str) -> Dict[str, List[str]]:
        elementos = {'conceptos': [], 'movimientos': [], 'problemas': [], 'ejemplos': []}
        
        # Conceptos de todos los capítulos
        conceptos_clave = [
            # Capítulo I
            'inmediatez', 'ser', 'esto', 'ahora', 'aquí', 'yo', 'universal', 'singular',
            'lenguaje', 'mostrar', 'haber sido', 'noche', 'día', 'árbol', 'casa', 'papel',
            # Capítulo II
            'percepción', 'cosa', 'propiedad', 'cualidades', 'uno', 'también', 'multiplicidad',
            'médium', 'coexistencia', 'cosidad', 'sal', 'blanca', 'salino', 'cúbica', 'peso',
            'esencial', 'no esencial', 'ser para sí', 'ser para otro', 'en tanto que',
            'determinabilidad', 'excluyente', 'universalidad sensible', 'materias',
            'reflexión', 'aprehensión', 'ilusión', 'buen sentido', 'abstracciones vacías',
            # Capítulo III
            'universal incondicionado', 'fuerza', 'exteriorización', 'juego de fuerzas', 'solicitación',
            'mundo suprasensible', 'interior', 'fenómeno', 'manifestación', 'apariencia',
            'ley', 'atracción universal', 'tautología', 'explicación', 'reino de las leyes',
            'mundo invertido', 'inversión', 'infinitud', 'autoconciencia',
            'diferencia', 'contradicción', 'negación', 'concepto', 'entendimiento',
            'electricidad', 'positiva', 'negativa', 'gravedad', 'caída', 'tiempo', 'espacio',
            'distancia', 'velocidad', 'polo norte', 'polo sur', 'brújula', 'oxígeno', 'hidrógeno',
            'venganza', 'castigo', 'perdón', 'auto-conciencia', 'reflexión'
        ]
        for c in conceptos_clave:
            if c in contenido.lower():
                elementos['conceptos'].append(c)
        
        # Detectar movimientos dialécticos
        if 'no es' in contenido.lower() and 'sino' in contenido.lower():
            elementos['movimientos'].append('negación determinada')
        if 'por tanto' in contenido.lower():
            elementos['movimientos'].append('conclusión dialéctica')
        if 'experiencia' in contenido.lower():
            elementos['movimientos'].append('experiencia de la conciencia')
        if 'también' in contenido.lower() and 'uno' in contenido.lower():
            elementos['movimientos'].append('oscilación uno/también')
        if 'en tanto que' in contenido.lower():
            elementos['movimientos'].append('recurso del en tanto que')
        if 'ser para sí' in contenido.lower() and 'ser para otro' in contenido.lower():
            elementos['movimientos'].append('coincidencia de opuestos')
        if 'se derrumba' in contenido.lower() or 'se supera' in contenido.lower():
            elementos['movimientos'].append('superación')
        if 'fuerza' in contenido.lower() and 'exteriorización' in contenido.lower():
            elementos['movimientos'].append('manifestación de la fuerza')
        if 'solicit' in contenido.lower():
            elementos['movimientos'].append('solicitación mutua')
        if 'ley' in contenido.lower() and ('tautología' in contenido.lower() or 'constante' in contenido.lower()):
            elementos['movimientos'].append('tautología legal')
        if 'mundo suprasensible' in contenido.lower():
            elementos['movimientos'].append('postulación del más allá')
        if 'invertido' in contenido.lower() or 'inversión' in contenido.lower():
            elementos['movimientos'].append('inversión dialéctica')
        if 'negación de la negación' in contenido.lower() or 'infinitud' in contenido.lower():
            elementos['movimientos'].append('infinitud')
        if 'explicación' in contenido.lower():
            elementos['movimientos'].append('explicación tautológica')
        
        # Ejemplos sensibles
        ejemplos_sensibles = ['dulce', 'amargo', 'negro', 'blanco', 'norte', 'sur', 'oxígeno', 
                              'hidrógeno', 'venganza', 'castigo', 'sal', 'árbol', 'casa', 'papel',
                              'imán', 'electricidad']
        for p in ejemplos_sensibles:
            if p in contenido.lower():
                elementos['ejemplos'].append(p)
        
        return elementos

    def detectar_transicion(self, contenido: str) -> Optional[str]:
        indicadores = {
            'con esto pasamos': 'Percepción → Entendimiento',
            'la nueva figura': 'transición genérica',
            'universalidad incondicionada': 'Entendimiento',
            'reino del entendimiento': 'Entendimiento',
            'fuerza y entendimiento': 'Entendimiento',
            'mundo suprasensible': 'Mundo suprasensible',
            'el mundo invertido': 'Mundo invertido',
            'infinitud': 'Infinitud',
            'la autoconciencia': 'Autoconciencia'
        }
        for señal, destino in indicadores.items():
            if señal in contenido.lower():
                return destino
        return None

    def procesar_fragmento(self, archivo_id: str, contenido: str, titulo_capitulo: Optional[str] = None) -> Dict:
        conexion = self.establecer_conexion(contenido, self.ultimo_contexto)
        elementos = self.extraer_elementos(contenido)
        self.conceptos_activos.update(elementos['conceptos'])

        reglas_aplicadas = []
        if self.rule_engine:
            reglas_aplicadas = self.rule_engine.verificar_fragmento(contenido, self.ultimo_contexto or {})

        transicion = self.detectar_transicion(contenido)
        if transicion:
            self.estado_actual = transicion

        entrada = {
            'archivo': archivo_id,
            'capitulo': titulo_capitulo,
            'conexion': conexion,
            'conceptos_nuevos': elementos['conceptos'],
            'movimientos': elementos['movimientos'],
            'ejemplos': elementos['ejemplos'],
            'reglas_aplicadas': reglas_aplicadas,
            'transicion_detectada': transicion,
            'perspectiva': self.perspectiva,
            'timestamp': datetime.now().isoformat()
        }
        self.linea_dialectica.append(entrada)
        self.ultimo_contexto = {
            'ultimo_tema': elementos['conceptos'][-1] if elementos['conceptos'] else 'indefinido',
            'ultimo_movimiento': elementos['movimientos'][-1] if elementos['movimientos'] else None,
            'archivo': archivo_id,
            'transicion': transicion
        }
        return entrada

    def resumen_hasta_ahora(self) -> Dict:
        return {
            'estado': self.estado_actual,
            'total_fragmentos': len(self.linea_dialectica),
            'conceptos_activos': list(self.conceptos_activos),
            'ultimo_movimiento': self.linea_dialectica[-1] if self.linea_dialectica else None,
            'perspectiva_actual': self.perspectiva
        }

    def exportar_a_dot(self, ruta: str):
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write("digraph CaminoFenomenologico {\n")
            f.write("  rankdir=LR;\n")
            f.write("  node [shape=box, style=filled, fillcolor=lightyellow];\n")
            for i, paso in enumerate(self.linea_dialectica):
                conceptos = ", ".join(paso['conceptos_nuevos'][:3]) if paso['conceptos_nuevos'] else "sin conceptos"
                nodo = f"  paso_{i} [label=\"{paso['capitulo']}\\n{conceptos}\"];\n"
                f.write(nodo)
                if i > 0:
                    label = paso['conexion'][:30] if paso['conexion'] else "continúa"
                    f.write(f"  paso_{i-1} -> paso_{i} [label=\"{label}\"];\n")
            f.write("}\n")
        print(f"✅ Grafo exportado a {ruta}")


# -------------------------------------------------------------------
# SISTEMA FENOMENOLÓGICO PRINCIPAL
# -------------------------------------------------------------------
class SistemaFenomenologico:
    """Sistema base que registra el movimiento dialéctico de la conciencia."""

    def __init__(self):
        self.estado = "BOOTING"
        self.bitacora: List[str] = []
        self.contradicciones: List[ContradiccionDict] = []
        self.figuras: Dict[str, FiguraPhenomenologica] = {}
        self.camino_conciencia: List[TransicionDict] = []
        self.ultima_figura_id: Optional[str] = None
        self.config: Dict[str, Any] = {}

    def cargar_configuracion(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.estado = "READY"
        print("✅ Sistema fenomenológico inicializado.")

    def ejecutar_prueba_certeza(self):
        contradiccion: ContradiccionDict = {
            'id': 'CS-001',
            'tipo': 'AUTO_CONTRA_DICHA',
            'descripcion': 'Brecha entre pretensión (riqueza infinita) y realidad (abstracción vacía)',
            'detalle': {
                'pretende': 'Expresar singularidad concreta',
                'puede': 'Solo enunciar universalidad abstracta ("es")'
            }
        }
        self.contradicciones.append(contradiccion)
        self.bitacora.append("PRIMERA CONTRADICCIÓN: Certeza sensible no puede hacer lo que dice.")
        return self.contradicciones

    def transicionar(self, nuevo_estado: str, razon: str):
        transicion: TransicionDict = {
            'desde': self.estado,
            'hacia': nuevo_estado,
            'razon': razon,
            'timestamp': datetime.now().isoformat()
        }
        self.camino_conciencia.append(transicion)
        self.estado = nuevo_estado
        self.bitacora.append(f"TRANSICIÓN: {razon}")

    def guardar_estado(self, ruta: Union[str, Path]):
        data = {
            "estado": self.estado,
            "bitacora": self.bitacora,
            "contradicciones": self.contradicciones,
            "figuras": {k: v.to_dict() for k, v in self.figuras.items()},
            "camino_conciencia": self.camino_conciencia,
            "ultima_figura_id": self.ultima_figura_id,
            "config": self.config
        }
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ Estado guardado en {ruta}")

    @classmethod
    def cargar_estado(cls, ruta: Union[str, Path]) -> 'SistemaFenomenologico':
        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)
        sistema = cls()
        sistema.estado = data["estado"]
        sistema.bitacora = data["bitacora"]
        sistema.contradicciones = data["contradicciones"]

        for k, v in data["figuras"].items():
            fig = FiguraPhenomenologica(
                id=v["id"],
                nombre=v["nombre"],
                tipo_figura=FiguraConciencia(v["tipo_figura"]),
                etapa=EtapaFenomenologica(v["etapa"]),
                texto_original=v.get("texto_original", ""),
                experiencia_conciencia=v.get("experiencia_conciencia", ""),
                verdad_aparece=v.get("verdad_aparece", ""),
                verdad_real=v.get("verdad_real", ""),
                contradiccion_interna=v.get("contradiccion_interna", ""),
                superacion_hacia=v.get("superacion_hacia", []),
                leccion_dialectica=v.get("leccion_dialectica", ""),
                referencias=v.get("referencias", {}),
                metáforas_clave=v.get("metáforas_clave", []),
                notas_analisis=v.get("notas_analisis", []),
                perspectiva=v.get("perspectiva", "para nosotros"),
                ejemplos_concretos=v.get("ejemplos_concretos", []),
                momentos_dialecticos=v.get("momentos_dialecticos", []),
                ironia_linguistica=v.get("ironia_linguistica", ""),
                perspectiva_dual=v.get("perspectiva_dual", {})
            )
            sistema.figuras[k] = fig

        sistema.camino_conciencia = data["camino_conciencia"]
        sistema.ultima_figura_id = data["ultima_figura_id"]
        sistema.config = data["config"]
        sistema.estado = data["estado"]
        print(f"✅ Estado cargado desde {ruta}")
        return sistema


class SistemaFenomenologicoMejorado(SistemaFenomenologico):
    """Extiende el sistema con capacidades predictivas."""

    def __init__(self):
        super().__init__()
        self.capacidades_nuevas = {
            'experimentacion_dialectica': True,
            'analisis_temporal': True,
            'deteccion_universalizacion': True,
            'motor_reglas': True
        }

    def predecir_proximo_paso(self, desde_estado: str) -> Dict[str, str]:
        predicciones = {
            'Certeza sensible': {
                'proximo': 'Percepción',
                'razon': 'La conciencia busca un objeto mediado pero estable (cosa con propiedades).',
                'conceptos': ['cosa', 'propiedades', 'uno', 'también']
            },
            'Percepción': {
                'proximo': 'Entendimiento',
                'razon': 'La cosa se descompone en contradicción (uno/múltiple, esencial/accidental, ser para sí/ser para otro).',
                'conceptos': ['fuerza', 'ley', 'mundo suprasensible']
            },
            'Entendimiento': {
                'proximo': 'Mundo suprasensible',
                'razon': 'El juego de fuerzas conduce al interior de las cosas.',
                'conceptos': ['interior', 'fenómeno']
            },
            'Mundo suprasensible': {
                'proximo': 'Mundo invertido',
                'razon': 'El mundo suprasensible se revela como vacío y se invierte.',
                'conceptos': ['inversión', 'diferencia pura']
            },
            'Mundo invertido': {
                'proximo': 'Infinitud',
                'razon': 'La inversión se sobrepasa a sí misma en la infinitud.',
                'conceptos': ['negación de la negación']
            },
            'Infinitud': {
                'proximo': 'Autoconciencia',
                'razon': 'La infinitud es el concepto de la autoconciencia.',
                'conceptos': ['yo', 'deseo', 'vida']
            }
        }
        return predicciones.get(desde_estado, {'proximo': 'desconocido'})


# -------------------------------------------------------------------
# DATOS DEL CAPÍTULO I (FRAGMENTOS)
# -------------------------------------------------------------------

FRAGMENTOS_CAPITULO1 = [
    {
        "id": "cs01",
        "pagina": 63,
        "texto": """I. LA CERTEZA SENSIBLE O EL ESTO Y LA SUPOSICIÓN
El saber, que es ante todo o de modo inmediato nuestro objeto, no puede ser sino aquello que es él mismo saber inmediato, saber de lo inmediato o de lo que es. Debemos mantener aquí un comportamiento igualmente inmediato o receptivo, es decir, no alterar nada en este saber tal y como se nos ofrece y mantener la aprehensión completamente aparte de la concepción.
El contenido concreto de la certeza sensible hace que ésta sea manifiesta de un modo inmediato como el conocimiento más rico e incluso como un conocimiento de riqueza infinita a la que no es posible encontrar límite si vamos más allá en el espacio y en el tiempo en que se despliega, como si tomásemos un fragmento de esta plenitud y penetrásemos en él mediante la división. Este conocimiento se manifiesta, además, como el más verdadero, pues aún no ha dejado a un lado nada del objeto, sino que lo tiene ante sí en toda su plenitud.
Pero, de hecho, esta certeza se muestra ante sí misma como la verdad más abstracta y más pobre. Lo único que enuncia de lo que sabe es esto: que es; y su verdad contiene solamente el ser de la cosa.
La conciencia, por su parte, es en esta certeza solamente como puro yo, y yo soy en ella solamente como puro éste y el objeto, asimismo, como puro esto. Yo, éste, no estoy cierto de esta cosa porque me haya desarrollado aquí como conciencia y haya puesto en marcha el pensamiento de diversos modos. Ni tampoco porque la cosa de que estoy cierto sea en ella misma, atendiendo a multitud de diversas cualidades, una relación plena de riqueza o un múltiple comportamiento con respecto a otras. Nada de esto interesa a la verdad de la certeza sensible; ni el yo ni la cosa tienen aquí la significación de una mediación múltiple; el yo no significa un representarse o un pensar múltiple, ni la cosa tiene la significación de múltiples cualidades, sino que la cosa es, y es solamente porque es; ella es: he ahí lo esencial para el saber sensible, y este puro ser o esta inmediata simple constituye la verdad de la cosa. Y asimismo la certeza, como relación, es una pura relación inmediata: la conciencia es yo y nada más, un puro éste; el singular sabe un puro esto o lo singular.
Pero, si nos fijamos atentamente, vemos que en el puro ser, que constituye la esencia de esta certeza y que ésta enuncia como su verdad, se halla en juego mucho más. Una certeza sensible real no es..."""
    },
    {
        "id": "cs02",
        "pagina": 64,
        "texto": """solamente esta pura inmediatez, sino un ejemplo de ella. Entre las innumerables diferencias que aquí se presentan encontramos en todos los casos la distinción fundamental, a saber: la de que en esta certeza quedan en seguida fuera del puro ser los dos estos mencionados, el éste como yo y el esto como objeto. Y si nosotros reflexionamos acerca de esta diferencia, vemos que ni el uno ni lo otro son en la certeza sensible solamente como algo inmediato, sino, al mismo tiempo, como algo mediado; yo tengo la certeza por medio de un otro, que es precisamente la cosa; y ésta, a su vez, es en la certeza por medio de un otro, que es precisamente el yo.

[1. El objeto de esta certeza]

Esta diferencia entre la esencia y el ejemplo, entre la inmediatez y la mediación, no la establecemos solamente nosotros, sino que la encontramos en la certeza sensible misma, y debemos acogernos en la forma como está en ella y no tal y como nosotros acabamos de determinarla. En ella, lo uno está puesto como lo que es de un modo simple e inmediato o como la esencia, es el objeto; en cambio, lo otro lo está como lo no esencial y mediado, que es allí no en sí, sino por medio de un otro, el yo, un saber que sólo sabe el objeto porque él es y que puede ser o no ser. Pero el objeto es, es lo verdadero y la esencia; es indiferente a ser sabido o no; y permanece aunque no sea sabido; en cambio, el saber no es si el objeto no es.

Deberá, pues, considerarse el objeto para ver si es, en realidad, en la certeza sensible misma, una esencia como la que pretende ser; si este su concepto de ser esencia corresponde al modo como se halla presente en dicha certeza. Para lo cual no debemos pararnos a reflexionar y meditar sobre lo que en verdad pueda ser, sino considerarlo solamente tal y como la certeza sensible lo tiene en ella.

Hay que preguntarle, por tanto, a ella misma: ¿qué es el esto? Si lo tomamos bajo la doble figura de su ser como el ahora y el aquí, la dialéctica que lleva en él cobrará una forma tan inteligible como el esto mismo. A la pregunta de ¿qué es el ahora? contestaremos, pues, por ejemplo: el ahora es la noche. Para examinar la verdad de esta certeza sensible, bastará un simple intento. Escribiremos esta verdad; una verdad nada pierde con ser puesta por escrito, como no pierde nada tampoco con ser conservada. Pero si ahora, este mediodía revisamos esta verdad escrita, no tendremos más remedio que decir que dicha verdad ha quedado ya vacía.

El ahora que es la noche se conserva, es decir, se le trata como aquello por lo que se hace pasar, como algo que es; pero se muestra..."""
    },
    {
        "id": "cs03",
        "pagina": 65,
        "texto": """más bien como un algo que no es. El ahora mismo se mantiene, sin duda, pero como algo que no es noche; y asimismo se mantiene con respecto al día que ahora es como algo que no es tampoco día o como un algo negativo en general. Por tanto, este ahora que se mantiene no es algo inmediato, sino algo mediado, pues es determinado como algo que permanece y se mantiene por el hecho de que un otro, a saber, el día y la noche, no es. Lo que no impide que siga siendo tan simplemente como antes, el ahora y que sea, en esta simplicidad, indiferente hacia lo que sigue sucediendo en torno a él; del mismo modo que la noche y el día no son su ser, tampoco él es día ni noche; no le afecta para nada este su ser otro. A este algo simple, que es por medio de la negación, que no es esto ni aquello, un no esto al que es también indiferente el ser esto o aquello, lo llamamos un universal; lo universal es, pues, lo verdadero de la certeza sensible.

Como un universal enunciamos también lo sensible; lo que decimos es: esto, es decir, el esto universal, o: ello es, es decir, el ser en general. Claro está que no nos representamos el esto universal o el ser en general, pero enunciamos lo universal; o bien no nos expresamos sencillamente tal como lo suponemos en esta certeza sensible. Pero, como advertimos, el lenguaje es lo más verdadero; nosotros mismos refutamos inmediatamente en él nuestra suposición, y como lo universal es lo verdadero de la certeza sensible y el lenguaje sólo expresa este algo verdadero, no es en modo alguno posible decir nunca un ser sensible que nosotros suponemos.

Y lo mismo ocurrirá con la otra forma del esto, con el aquí. El aquí es, por ejemplo, el árbol. Pero si doy la vuelta, esta verdad desaparece y se trae a lo contrario: el aquí no es un árbol, sino que es una casa. El aquí mismo no desaparece, sino que es permanentemente en la desaparición de la casa, del árbol, etc., indiferente al hecho de ser casa, árbol, etc. El esto se revela, de nuevo, pues, como una simplicidad mediada o como universalidad.

La certeza sensible, al mostrar en ella misma lo universal como la verdad de su objeto, permanece, por tanto, el ser puro como su esencia, pero no como algo inmediato, sino [como] algo a lo que es esencial la negación y la mediación y, por consiguiente, no como lo que nosotros suponemos como el ser, sino como el ser determinado como la abstracción o lo universal puro; y nuestra suposición, para la que lo verdadero de la certeza sensible no es lo universal es lo único que queda frente a ese ahora y aquí vacíos o indiferentes.

Si comparamos la relación en que primeramente surgían el saber y el objeto con la relación bajo la que se presentan en este resultado, los términos se invierten. El objeto, que debiera ser lo esencial, pasa..."""
    },
    {
        "id": "cs04",
        "pagina": 66,
        "texto": """a ser ahora lo no esencial de la certeza sensible, pues lo universal en que se ha convertido no es ya tal y como el objeto debiera ser esencial para ella, sino que ahora se hace presente en lo contrario, es decir, en el saber, que antes era lo no esencial. Su verdad está en el objeto como mi objeto o en la suposición; es porque yo sé de él. Por tanto, la certeza sensible, aunque haya sido desalojada del objeto, no por ello ha sido superada, sino que se ha limitado a replegarse en el yo; y queda por ver todavía lo que la experiencia nos indica acerca de esta su realidad.

[2. El sujeto de esta certeza]

La fuerza de su verdad reside ahora, pues, en el yo, en la inmediatez de mi vista, de mi oído, etc.; la desaparición del ahora y el aquí singulares que nosotros suponemos se evita porque yo los tengo. El ahora es día porque yo lo veo; el aquí es un árbol por lo mismo. Pero la certeza sensible en esta relación experimenta en sí misma la misma dialéctica que en la relación anterior. Yo, éste, veo el árbol y afirmo el árbol como el aquí; pero otro yo ve la casa y afirma que el aquí no es un árbol, sino que es la casa. Ambas verdades encierran el mismo título de legitimidad, que es el carácter inmediato del ver y la seguridad y la aseveración de ambas en cuanto a su saber; pero una de ellas desaparece en la otra.

Lo que aquí no desaparece es el yo, en cuanto universal, cuyo ver no es un ver del árbol ni de esta casa, sino un simple ver mediado por la negación de esta casa, etc., y que en ello se mantiene igualmente simple e indiferente ante lo que en torno a ella sucede, ante la casa o el árbol. El yo sólo es universal, como ahora, aquí o éste, en general; cierto es que lo que supongo es un yo singular, pero del mismo modo que no podemos decir lo que suponemos en el aquí y el ahora, no podemos decir tampoco lo que suponemos en el yo. Al decir este aquí, este ahora, algo singular, digo todos los estos, los aquí, los ahora, los singulares; y lo mismo, al decir yo digo este yo singular, digo en general, todos los yo; cada uno de ellos es lo que digo: yo, este yo singular. Y cuando se exige de la ciencia como su piedra de toque a la que sencillamente no podría hacer frente, que deduzca, construya o descubra a priori, o como ello quiera expresarse, una llamada extra cosa o un arte hombre, sería obligado que quienes tal exigen dijeran qué esta cosa o qué este yo suponen; pero decir esto es imposible."""
    },
    {
        "id": "cs05",
        "pagina": 67,
        "texto": """[3. La experiencia de esta certeza]

La certeza sensible experimenta, pues, que su esencia no está ni en el objeto ni en el yo y que la inmediatez no es la inmediatez del uno ni la del otro, pues en ambos lo que supongo es más bien algo inesencial, y el objeto y el yo son lo universal en lo que no permanece o es aquel ahora y aquí y aquel yo que yo supongo. Por donde llegamos al resultado de poner la totalidad de la certeza sensible misma como su esencia, y no ya sólo un momento de ella, como sucedía en los dos casos anteriores, en que su realidad debía ser primeramente el objeto contrapuesto al yo y luego el yo. Así, pues, sólo es la certeza sensible misma en su totalidad la que se mantiene en ella como inmediatez, excluyendo así de ella toda la contraposición que en lo anterior se encontraba.

Por consiguiente, a esta inmediatez pura no interesa ya para nada el ser otro del aquí como árbol que se toma en un aquí que es un no-árbol, el ser otro del ahora como día que se toma en un ahora que es noche u otro yo para el que un otro es objeto. Su verdad se mantiene como una relación que permanece igual a sí misma que no establece entre el yo y el objeto diferencia alguna con respecto a lo esencial y lo no esencial y en la que, por tanto, no puede tampoco deslizarse ninguna diferencia. Yo, éste, afirmo por consiguiente el aquí como árbol y no me vuelvo, evitando con ello que el aquí se convierta para mí en un no-árbol; ni me entero tampoco de que otro yo ve el aquí como no-árbol o de que yo mismo tomo en otra situación el aquí como no-árbol o el ahora como no-día, sino que yo soy puro intuir; yo, para mí, me mantengo en que el ahora es día o en que el aquí es árbol, y no comparo tampoco entre sí el aquí y el ahora, sino que me mantengo en una relación inmediata: el ahora es día.

Y, como, según esto, esta certeza se niega ya a salir de sí cuando llamamos su atención hacia un ahora que es noche o hacia un yo para quien es noche, vamos nosotros hacia ella y hacemos que se nos muestre el ahora que se afirma. Y tenemos que dejar que se nos muestre, pues la verdad de esta relación inmediata es la verdad de este yo, que se circunscribe a un ahora o un aquí. Si después asumiésemos esta verdad o nos mantuviésemos alejados de ella, carecería ya de toda significación, pues superaríamos con ello la inmediatez que le es esencial. Debemos, por tanto, colocarnos en el mismo punto del tiempo o del espacio, hacer que se nos muestre, es decir, convertirnos en este mismo yo que es el que sabe con certeza. Veamos, pues, cómo está constituido lo inmediato que se nos muestra.

Se muestra el ahora, este ahora. Ahora; cuando se muestra, ya ha dejado de ser; el ahora que es, es otro del que se muestra, y vemos que el ahora es precisamente esto: en el momento en que es, no ser ya. El ahora, tal y como se nos mostró, es un algo que ha sido, y esto es su verdad: no tiene la verdad de ser. Es, pues, verdad que es algo que fue. Pero lo que fue no es, de hecho, esencia; lo que no es, es lo que nos interesa."""
    },
    {
        "id": "cs06",
        "pagina": 68,
        "texto": """dejado de existir; el ahora que es ya otro ahora que el que se muestra y vemos que el ahora consiste precisamente, en cuanto es, en no ser ya. El ahora tal como se nos muestra, es algo que ha sido, y ésta es su verdad; no tiene la verdad del ser. Su verdad consiste, sin embargo, en haber sido. Pero lo que ha sido no es, de hecho, una esencia; no es, y de lo que se trataba era del ser.

En esta indicación vemos, pues, solamente un movimiento cuya trayectoria es la siguiente: 1º Indico el ahora, que se afirma como lo verdadero, pero lo indico como algo que ha sido o como algo superado, con lo que supero la primera verdad. 2º Ahora, afirmo como la segunda verdad que lo que ha sido está superado. 3º Pero lo que ha sido no es; supero lo que ha sido o el ser superado, o sea la segunda verdad, negando con ello la negación del ahora y retomando así a la primera afirmación: el ahora es. El ahora y la indicación del ahora están constituidos, pues, de tal modo que ni el ahora ni la indicación del ahora son algo inmediatamente simple, sino un movimiento que lleva en sí momentos distintos; se pone el esto, pero lo que se pone es más bien un otro o el esto es superado; y este ser otro o superación de lo primero es nuevamente superado, a su vez, retornándose así a lo primero. Pero este primero reflejado en sí no es exactamente lo mismo que primeramente era, es decir, algo inmediato, sino que es cabalmente algo reflejado en sí o algo simple, que permanece en el ser otro lo que es: un ahora que es absolutamente muchos ahora; y esto es el verdadero ahora, el ahora como día simple, que lleva en sí muchos ahora, muchas horas; y un tal ahora, una hora, es también muchos minutos, y este ahora es, asimismo, muchos ahora, y así sucesivamente. La indicación es, pues, ella misma el movimiento que expresa lo que el ahora es en verdad, es decir, un resultado o una pluralidad de ahoras compendiada; y la indicación es la experiencia de que el ahora es universal.

El aquí indicado que yo retengo es también un este aquí que de hecho no es este aquí, sino un delante y un detrás, un arriba y un abajo, un a la derecha y a la izquierda. El arriba es, a su vez, también este múltiple ser otro en el arriba, el abajo, etc. El aquí que se trataba de indicar desaparece en otros aquí, pero también éstos, a su vez, desaparecen; lo indicado, retenido y permanente es un esto negativo, que sólo es en cuanto que los aquí se tornan como deben tomarse, pero superándose en ello; es un simple conjunto de muchos aquí...El aquí supuesto sería el punto; pero éste no es, sino que, al indicárselo como lo que es, la indicación no se muestra como un saber inmediato, sino como un movimiento que, partiendo del aquí supuesto, conduce a través de muchos aquí al aquí universal, que es..."""
    },
    {
        "id": "cs07",
        "pagina": 69,
        "texto": """una simple multiplicidad de aquí, lo mismo que el día es una multiplicidad de ahora.

Es claro que la dialéctica de la certeza sensible no es sino la simple historia de su movimiento o de su experiencia y, a su vez, la certeza sensible misma no es sino esta historia. La conciencia natural llega, por ello, siempre, por sí misma, a este resultado, lo que en ella es lo verdadero y hace la experiencia de ello; pero en seguida vuelve a olvidarlo y reinicia el movimiento desde el principio. Es, pues, sorprendente que, frente a esta experiencia, se presente como experiencia universal y también como afirmación filosófica y hasta como resultado del escepticismo, el que la realidad o el ser de las cosas exteriores, en cuanto estos o cosas sensibles, tiene verdad absoluta para la conciencia. Semejante afirmación no sabe lo que dice, ni sabe que dice cabalmente lo contrario de lo que se propone decir. La verdad del esto sensible para la conciencia debe ser experiencia universal, pero resulta que la experiencia universal es más bien lo contrario; toda conciencia supera a su vez una tal verdad, como por ejemplo el aquí es un árbol o el ahora es mediodía, y expresa lo contrario de ello: el aquí no es un árbol, sino una casa; y lo que en esta afirmación, que supera la primera, es a su vez una afirmación semejante de un esto sensible lo supera también inmediatamente; y así, en toda certeza sensible sólo se experimenta en verdad lo que hemos visto, es decir, el esto precisamente como un universal, lo contrario de lo que aquella afirmación asegura que es la experiencia universal. Y, al remitirnos a la experiencia universal, se nos permitirá que nos anticipemos a la consideración de lo práctico. A este respecto, cabe decir a quienes afirman aquella verdad y certeza de la realidad [Realitat] de los objetos sensibles que debieran volver a la escuela más elemental de la sabiduría, es decir, a los antiguos misterios eleusinos de Ceres y Baco, para que empezaran por aprender el misterio del pan y el vino, pues el iniciado en estos misterios no sólo se elevaba a la duda acerca del ser de las cosas sensibles, sino a la desesperación de él, ya que, por una parte, conserva en ellas su aniquilación, mientras que, por otra parte, las veía aniquilarse a ellas mismas. Tampoco los animales se hallan excluidos de esta sabiduría, sino que, por el contrario, se muestran muy profundamente iniciados en ella, pues no se detienen ante las cosas sensibles como si fuesen cosas en sí, sino que, desesperando de esta realidad [Realitat] y en la plena certeza de su nulidad, se apoderan de ellas sin más y las devoran; y toda la naturaleza celebra, como ellos, estos misterios revelados, que enseñan cuál es la verdad de las cosas sensibles."""
    },
    {
        "id": "cs08",
        "pagina": 70,
        "texto": """Sin embargo, también quienes formulan semejante afirmación dicen, con arreglo a las anteriores observaciones, directamente lo contrario de lo que suponen, y este fenómeno es tal vez el que mejor se presta a llevarnos a reflexionar acerca de la naturaleza de la certeza sensible. Hablan de la existencia de los objetos externos, que cabe determinar todavía con mayor precisión como cosas reales, absolutamente singulares, totalmente personales e individuales, cada una de las cuales no tiene ya su igual absoluto, y dicen que esa existencia posee certeza y verdad absolutas. Suponen este trozo de papel en que escribo, o mejor dicho he escrito, esto; pero no dicen lo que suponen. Si realmente quisieran decir este trozo de papel que suponen y esto es lo que quieren decir esto es imposible, ya que el esto sensible supuesto es inasequible al lenguaje, que pertenece a la conciencia, a lo universal en sí. Por tanto, bajo el intento real de decirlo se desintegra; quienes comenzaran a describirlo no podrían acabar su descripción, sino que deberían dejarlo a cargo de otros, los cuales tendrían que reconocer ellos mismos, a la postre, que hablaban de una cosa que no es. Suponen, por tanto, indudablemente, este trozo de papel, que aquí es completamente otro que el de arriba; pero hablan de “cosas reales, de objetos externos o sensibles, de esencias absolutamente individuales”, etc.; es decir, sólo dicen de ellos lo universal; por tanto, lo que se llama lo inexpresable no es sino lo no verdadero, lo no racional, lo simplemente supuesto. Si no decimos de algo sino que es una cosa real, un objeto externo, no decimos solamente lo más universal de todo, y de este modo enunciamos más bien en su igualdad con todo que su diferenciabilidad. Si digo una cosa singular, la digo más bien como totalmente universal, pues todo es una cosa singular; lo mismo que esta cosa es todo lo que se quiera. Y si, más exactamente, se indica este trozo de papel, tendremos que todo papel es un acto trozo de papel, y yo he dicho siempre solamente lo universal. Pero, si quiero echar mano del discurso, que tiene la naturaleza divina de invertir inmediatamente la suposición para convertirla en algo distinto y no dejar, así, que se exprese en modo alguno en palabras, puedo indicar este trozo de papel, y hago entonces la experiencia de lo que es de hecho la verdad de la certeza sensible: lo indico como un aquí que es un aquí de otros aquí o en él mismo un simple conjunto de muchos aquí; es decir, que es un universal; lo tomo tal y como es en verdad y, en vez de saber algo inmediato, lo percibo."""
    }
]

# Notas de análisis del Capítulo I
NOTAS_CERTEZA_SENSIBLE = {
    "cs01": "Fragmento cs01 (p63): Pretensión de inmediatez y riqueza, pero resulta abstracta.",
    "cs02": "Fragmento cs02 (p64): Distinción yo-objeto; prueba del ahora con escritura.",
    "cs03": "Fragmento cs03 (p65): Prueba del aquí; el lenguaje dice lo universal; el esto es universal.",
    "cs04": "Fragmento cs04 (p66): Repliegue en el yo; el yo también es universal.",
    "cs05": "Fragmento cs05 (p67): Intento de mostrar el ahora; el ahora se desvanece.",
    "cs06": "Fragmento cs06 (p68): Multiplicidad de ahoras y aquíes; el ahora es universal.",
    "cs07": "Fragmento cs07 (p69): Conclusión: la certeza sensible es su historia; ironía de los animales y misterios eleusinos.",
    "cs08": "Fragmento cs08 (p70): Conclusión del capítulo. El ejemplo del trozo de papel muestra que lo singular es inexpresable; el lenguaje invierte la suposición. Transición explícita a la percepción."
}

# Ejemplos concretos del Capítulo I
EJEMPLOS_CERTEZA_SENSIBLE = {
    "cs02": [{"tipo": "ahora", "prueba": "noche", "refutacion": "mediodía"}],
    "cs03": [{"tipo": "aquí", "prueba": "árbol", "refutacion": "casa"}],
    "cs04": [{"tipo": "yo", "prueba": "yo veo árbol", "refutacion": "otro ve casa"}],
    "cs05": [{"tipo": "ahora mostrado", "prueba": "intento de mostrar el ahora", "refutacion": "cuando se muestra, ya ha dejado de ser"}],
    "cs08": [{"tipo": "trozo de papel", "prueba": "suponer este trozo de papel", "refutacion": "al decirlo, se dice universal"}]
}

# Momentos dialécticos del Capítulo I
MOMENTOS_CERTEZA_SENSIBLE = [
    "presentación de la inmediatez",
    "revelación de la abstracción",
    "distinción yo-objeto",
    "prueba del ahora",
    "escritura de la verdad",
    "prueba del aquí",
    "revelación del universal",
    "ironía del lenguaje",
    "repliegue en el yo",
    "contradicción entre yoes",
    "universalidad del yo",
    "totalidad de la certeza",
    "negativa a salir de sí",
    "fuerza del mostrarse",
    "desaparición del ahora",
    "multiplicidad de ahoras",
    "multiplicidad de aquíes",
    "lección de los animales",
    "imposibilidad de decir lo singular",
    "lenguaje divino (invierte la suposición)",
    "transición a la percepción"
]

# Metáforas clave del Capítulo I
METAFORAS_CERTEZA_SENSIBLE = [
    "inmediatez", "receptividad", "pureza", "riqueza infinita", "abstracción", "pobreza",
    "ahora", "noche", "día", "aquí", "árbol", "casa", "yo", "otro yo", "mostrar", "haber sido",
    "pan", "vino", "animales", "devorar", "trozo de papel"
]


# -------------------------------------------------------------------
# DATOS DEL CAPÍTULO II (FRAGMENTOS)
# -------------------------------------------------------------------

FRAGMENTOS_CAPITULO2 = [
    {
        "id": "p01",
        "pagina": 71,
        "texto": """II. LA PERCEPCIÓN, O LA COSA Y LA ILUSIÓN

La certeza inmediata no se posesiona de lo verdadero, pues su verdad es lo universal; pero quiere captar el esto. La percepción, por el contrario, capta como universal lo que para ella es lo que es. Y siendo la universalidad su principio en general lo son también los momentos que de un modo inmediato se distinguen en ella: el yo es un universal y lo es el objeto. Aquel principio nace para nosotros, por lo que nuestro modo de acoger la percepción no es ya un acoger que se manifiesta, como el de la certeza sensible, sino necesario. En el nacimiento del principio han devenido al mismo tiempo ambos momentos, que no hacen más que desdoblarse en su manifestación; uno de estos momentos es el movimiento de la indicación, el otro el mismo movimiento, pero como algo simple; aquél es la percepción, éste el objeto. El objeto es, conforme a la esencia, lo mismo que es el movimiento; éste es el despliegue y la distinción de los momentos, aquél la reunión de ellos. Para nosotros o en sí, es lo universal como principio la esencia de la percepción y, frente a esta abstracción, los dos términos diferenciados, el que percibe y lo percibido, son lo no esencial. Pero, de hecho, por cuanto que ambos son a su vez lo universal o la esencia, ambos son esenciales; pero en cuanto que se relacionan el uno con el otro como contrapuestos, en esta relación solamente el uno puede ser lo esencial, y la diferencia entre lo esencial y lo no esencial tiene que repartirse entre ellos. Lo uno determinado como lo simple, el objeto, es la esencia, a lo que es indiferente el hecho de que sea percibido o no; ahora bien, el percibir como el movimiento es lo inconstante, que puede ser o también no ser, y lo no esencial.

Este objeto debe determinarse ahora con mayor precisión y esta determinación debe desarrollarse brevemente partiendo del resultado obtenido; el desarrollo más detallado no es de este lugar. Como su principio, lo universal, es en su simplicidad algo mediano, el objeto debe expresar esto en él como su naturaleza, mostrándose así como la cosa de múltiples cualidades. La riqueza del saber sensible pertenece a la percepción, no a la certeza inmediata, en la que, según ya se vio, era solamente algo concomitante; pues solamente la percepción tiene en su esencia la negación, la diferencia o la multiplicidad."""
    },
    {
        "id": "p02",
        "pagina": 72,
        "texto": """[1. El concepto simple de la cosa]

El esto se pone, pues, como no esto o como superado y, por tanto, no como nada, sino como una nada determinada o una nada de un contenido, a saber, del esto. De este modo, sigue presente aquí lo sensible mismo, pero no como debiera serlo en la certeza inmediata, como lo singular supuesto, sino como universal o como lo que se determinará como propiedad. La superación presenta su verdadera doble significación, que hemos visto en lo negativo: es al mismo tiempo un negar y un mantener; la nada, como nada del esto, mantiene la inmediatez y es ella misma sensible, pero es una inmediatez universal. Pero el ser es un universal porque tiene en él la mediación o lo negativo; en cuanto expresa esto en su inmediatez, es una propiedad distinta, determinada. Con ello se ponen al mismo tiempo muchas propiedades de éstas, la una negativa de la otra. Al expresarse en la simplicidad de lo universal, estas determinabilidades, que en rigor sólo son propiedades por otra determinación que ha de añadirse, se relacionan consigo mismas, son indiferentes las unas con respecto a las otras y cada una de ellas es para sí y libre de las demás. Pero la universalidad simple igual a sí misma es, a su vez, distinta y libre de estas sus determinabilidades; es el puro relacionarse consigo mismo o el médium en que todas estas determinabilidades son, y en el que, por tanto, se compenetran en una unidad simple, pero sin entrar en contacto, pues precisamente por participar de esta universalidad son indiferentes para sí. Este médium universal abstracto, que puede ser llamado la coexistencia en general o la esencia pura, no es sino el aquí y el ahora, tal como se ha mostrado, o sea como un conjunto simple de muchos; pero estos muchos son ellos mismos, en su determinabilidad, universales simples. Esta sal es un aquí simple y, al mismo tiempo, múltiple; es blanca y es también de sabor salino, y es también de forma cúbica, posee también determinado peso, etc. Todas estas múltiples propiedades se dan en un simple aquí, en el que, por tanto, se compenetran; ninguna de ellas tiene un aquí distinto del de otra, sino que cada una de ellas se halla siempre en el mismo aquí que las demás; y, al mismo tiempo, sin hallarse separadas por distintos aquí, no se afectan las unas a las otras en esta compenetración; lo blanco no afecta o hace cambiar a lo cúbico, ni lo uno a lo otro al sabor salino, etc., sino que, siendo cada una de ellas, a su vez, un simple relacionarse consigo misma, deja tranquilas a las otras y sólo se relaciona con ellas por el indiferente también. Este también es, por tanto, el mismo puro universal o el médium, la cosidad que las reúne."""
    },
    {
        "id": "p03",
        "pagina": 74,
        "texto": """En esta conexión que así se desprende, sólo se observa y desarrolla, primeramente, el carácter de la universalidad positiva; pero se ofrece, además, otro lado que debe ser tomado también en consideración. En efecto, si las múltiples propiedades determinadas fuesen sencillamente indiferentes y sólo se refirieran a sí mismas, no serían propiedades determinadas; pues sólo lo son en cuanto se distinguen y se relacionan con otras como contrapuestas. Pero, con arreglo a esta contraposición, no pueden hallarse juntas en la unidad simple de su médium, la cual es tan esencial para ellas como la negación; por tanto, la distinción dentro de esta unidad, en cuanto no es una unidad indiferente, sino excluyente, que niega a otro, cae fuera de este médium simple; por consiguiente, éste no es solamente un también, unidad indiferente, sino que es, asimismo, uno, unidad excluyente. Lo uno es el momento de la negación, en cuanto se relaciona consigo mismo de un modo simple y excluye a otro y aquello que determina a la sociedad como cosa. En la cualidad, la negación es, como determinabilidad, inmediatamente una con la inmediatez del ser, la que por esta unidad con la negación, es universalidad; pero, como uno, se libera de esta unidad con lo contrario y es en y para sí misma.

En el conjunto de estos momentos se consuma la cosa como lo verdadero de la percepción, en la medida en que es necesario desarrollarlo aquí. Es a) la universalidad pasiva indiferente, el también de las múltiples propiedades o más bien materias, b) la negación asimismo como simple o lo uno, la exclusión de las propiedades contrapuestas, y c) las múltiples propiedades mismas, la relación entre los dos primeros momentos, la negación en cuanto se relaciona con el elemento indiferente y se expande en él como una multitud de diferencias, irradiándose el foco de la singularidad en la multiplicidad en el médium de lo subsistente. Por el lado en que estas diferencias pertenecen al médium indiferente, ellas mismas son universales, se relacionan solamente consigo mismas y no se afectan entre sí; en cambio, por el lado en que pertenecen a la unidad negativa, son al mismo tiempo excluyentes; pero esta relación de contraposición va aparejada necesariamente a propiedades alejadas de su también. La universalidad sensible o la unidad inmediata del ser y de lo negativo sólo es, así, propiedad en cuanto que el uno y la universalidad pura se desarrollan partiendo de ella y se distinguen entre sí y aquella universalidad sensible enlaza la una con la otra; sólo esta relación de dicha universalidad con los momentos esenciales puros es la que consuma la cosa."""
    },
    {
        "id": "p04",
        "pagina": 74,
        "texto": """[2. La percepción contradictoria de la cosa]

Así se halla, pues, constituida la cosa de la percepción; y la conciencia, en cuanto esta cosa es su objeto, se determina como conciencia percipiente; sólo tiene que captar este objeto y comportarse como pura aprehensión; lo que así obtiene es lo verdadero. Si la conciencia pusiera algo de su parte en esta aprehensión modificaría la verdad con lo que añadiese u omitiese. Siendo el objeto lo verdadero y lo universal lo igual a sí mismo, y la conciencia, en cambio, lo variable y lo no esencial, a ésta puede ocurrirle que aprehenda el objeto de un modo inexacto e incurra en ilusión. El que percibe tiene la conciencia de la posibilidad de la ilusión, pues en la universalidad, que es el principio, el ser otro mismo es inmediatamente para él, pero como lo nulo, como lo superado. Su criterio de verdad es, por tanto, la igualdad consigo mismo y su comportamiento aprehenderse como igual a sí mismo. Siendo la diversidad al mismo tiempo para quien percibe, su comportamiento es un relacionar entre sí los distintos momentos de su aprehensión; sin embargo, si en esta comparación se muestra una desigualdad, no se trata de una no-verdad del objeto, ya que éste es lo igual a sí mismo, sino de una no-verdad de la percepción.

Veamos ahora qué experiencia hace la conciencia en su percibir real. Esta experiencia se contiene ya para nosotros en el desarrollo ya dado del objeto y del comportamiento de la conciencia con respecto a él y será solamente el desarrollo de las contradicciones presentes en él. El objeto que yo capto se ofrece como un puro uno; mas yo descubro también en él la propiedad que es universal, pero que, por serlo, rebasa la singularidad. Por tanto, el primer ser de la esencia objetiva como un uno no era su verdadero ser; y, siendo el objeto lo verdadero, la no-verdad cae en mí, y la aprehensión no era acertada. La universalidad de la propiedad me obliga a captar la esencia objetiva más bien como una comunidad en general. Percibo, además, la propiedad como determinada, contrapuesta a otra y que la excluye. Por tanto, no aprehendía acertadamente la esencia objetiva cuando la determinaba como una comunidad con otras o como la continuidad, y debo más bien, en gracia a la determinabilidad de la propiedad, separar la continuidad y poner aquella esencia como uno excluyente. En el uno separado encuentro muchas propiedades de éstas que no se afectan unas a otras, sino que son indiferentes entre sí; por tanto, no percibía acertadamente el objeto cuando lo aprehendía como excluyente, sino que así como antes sólo era continuidad en general, ahora es un médium común universal en el que muchas propiedades, como universalidades sensibles, son cada una para sí y, como determinadas, excluyen a las otras. Pero, aun con esto, lo simple y lo verdadero que yo percibo no es tampoco un médium universal, sino la propiedad singular para sí, pero que así no es ni propiedad ni un ser determinado; pues ahora no es en un uno ni tampoco en relación con otros. Pero propiedad sólo lo es en el uno, y determinada solamente en relación con otros. Como este puro relacionarse consigo misma, ya no tiene en sí el carácter de la negatividad, permanece solamente como ser sensible en general; y la conciencia para la que ahora hay un ser sensible sólo es un suponer, es decir, ha salido completamente de la percepción y retornado a sí misma. Pero el ser sensible y el suponer se forman ellos mismos en la percepción; yo me veo repelido hacia el punto de partida y arrastrado de nuevo al mismo ciclo, que se supera en cada uno de sus momentos y como totalidad.

La conciencia vuelve, pues, a recorrer necesariamente este ciclo, pero, al mismo tiempo, no lo recorre ya del mismo modo que la primera vez. Ha pasado, en efecto, por la experiencia de que el resultado y lo verdadero del percibir son la disolución de la conciencia o la reflexión dentro de sí misma partiendo de lo verdadero. De este modo se ha determinado para la conciencia cómo se halla esencialmente constituido su percibir, a saber: no es una aprehensión pura y simple, sino que en su aprehensión la conciencia, al mismo tiempo, se refleja dentro de sí, partiendo de lo verdadero. Este retorno de la conciencia a sí misma, que se mezcla de modo inmediato en la pura aprehensión —y que se ha mostrado como algo esencial al percibir—, hace cambiar lo verdadero. La conciencia conoce este lado, al mismo tiempo, como el suyo y lo acoge, con lo cual se mantiene puro, por tanto, el verdadero objeto. Y así, encontramos ahora, como ocurriría en la certeza sensible, que se hace presente en el percibir el lado de que la conciencia se ve de nuevo empujada hacia sí misma, pero, de momento, no en el sentido en que allí acaece, como si la verdad del percibir cayera en ello, sino que conoce más bien lo que cae en ello, es la no-verdad allí presente. Ahora bien, a través de este conocimiento la conciencia es, al mismo tiempo, capaz de superar esa no-verdad; distingue su aprehensión de lo verdadero de la no-verdad de su percibir, corrige éste y, en cuanto emprende ella misma esta rectificación, cae en ella, evidentemente, la verdad, como verdad del percibir. El comportamiento de la conciencia que de aquí en adelante hay que considerar está constituido de tal modo, que ya no percibe simplemente, sino que es, además, consciente de su reflexión dentro de sí y separa esta reflexión de la simple aprehensión misma."""
    },
    {
        "id": "p05",
        "pagina": 76,
        "texto": """Así, pues, comienzo dándome cuenta de la cosa como uno y tengo que retenerla en esta determinación verdadera; si en el movimiento de la percepción se da algo contradictorio con aquella determinación, habrá que reconocerlo como mi reflexión. En la percepción se dan también, ahora, diferentes propiedades, que parecen ser propiedades de la cosa; sin embargo, la cosa es un uno, y tenemos la conciencia de que esa diferencia, con la que ha dejado de ser uno, recae en nosotros. Por tanto, esta cosa, de hecho, sólo es blanca puesta ante nuestros ojos y es también, de sabor salino, en contacto con nuestra lengua, y también de forma cúbica cuando nosotros la tocamos, etc. Toda la diversidad de estos lados no la sacamos de la cosa misma, sino de nosotros; y los lados se presentan diferenciados ante nuestras lenguas de un modo completamente distinto que ante nuestros ojos, etc. Somos nosotros, por consiguiente, el médium universal en el que esos momentos se separan y son para sí. Por tanto, por el hecho de considerar como nuestra reflexión la determinabilidad de ser médium universal, mantenemos la igualdad de la cosa consigo misma y la verdad de la cosa de ser un uno.

Pero estos diferentes lados que la conciencia asume, cada uno para sí, considerados como lados que se encuentran en el médium universal, son determinados; lo blanco es sólo por oposición a lo negro, etc., y la cosa es un uno precisamente porque se contrapone a otras. Pero, no excluye de sí a otras en cuanto es un uno, pues el ser uno es el universal relacionarse consigo mismo y por el hecho de ser un uno es más bien igual a todas, sino que las excluye por la determinabilidad. Así, pues, las cosas mismas son determinadas en y para sí; tienen propiedades mediante las cuales se diferencian de las demás. Y, siendo la propiedad la propiedad propia de la cosa o una determinabilidad en ella misma, la cosa tiene varias propiedades. En efecto, la cosa es, en primer lugar, lo verdadero, es en sí misma; y lo que es en ella es en ella misma como su propia esencia, y no en virtud de otras cosas; en segundo lugar, por tanto, las propiedades determinadas no sólo no son en virtud de otras cosas y para éstas, sino que son en ella misma; pero sólo son determinadas propiedades en ella en cuanto que son varias que se distinguen unas de otras; y, en tercer lugar, en cuanto que son así en la sociedad, son en y para sí e indiferentes las unas respecto a las otras. Es, en verdad, por consiguiente, la cosa misma la que es blanca y también cúbica, también de sabor salino, etc., o la cosa es el también o el médium universal en el que subsisten las múltiples propiedades las unas fuera de las otras, sin tocarse ni superarse; y así captada, la cosa se capta como lo verdadero.

Ahora bien, en este percibir, la conciencia es, al mismo tiempo, consciente de que se refleja también dentro de sí misma y de que en el percibir aparece el momento contrapuesto al también. Pero este momento es unidad de la cosa consigo misma, que excluye de sí la diferencia; es, por tanto, esta unidad la que la conciencia tiene que asumir, pues la cosa misma es la subsistencia de múltiples propiedades distintas e independientes. Por eso decimos de la cosa que es blanca, y también cúbica, y también de sabor salino, etc. Pero, en cuanto es blanca no es cúbica, y en cuanto es cúbica y también blanca, no es de sabor salino, etc. La unificación de estas propiedades corresponde solamente a la conciencia, la que, por consiguiente, no debe dejar que caigan como un uno en la cosa. Es para eso para lo que introduce el en tanto que, con lo que las separa y mantiene la cosa como el también. En rigor, la conciencia asume el ser uno solamente cuando aquello que llamábamos propiedad se representa como materia libre. La cosa se eleva de este modo a verdadero también al convertirse en una suma de materias y, en vez de ser un uno, pasa a ser solamente la superficie que las implica.

Si ahora volvemos la vista atrás para ver lo que la conciencia asumía antes y lo que asume ahora, lo que antes atribuía a las cosas y ahora se atribuye a sí, resulta que la conciencia hace alternativamente tanto de sí misma como también de la cosa el uno puro y sin multiplicidad como un también disuelto en materias independientes. La conciencia encuentra, pues, por medio de esta comparación, que no sólo su captar lo verdadero tiene en sí la diversidad de la aprehensión y del retorno a sí misma, sino más bien que lo verdadero mismo, la cosa, se muestra de este doble modo. Se da, así, la experiencia de que la cosa se presenta para la conciencia que la aprehende de un determinado modo, pero, al mismo tiempo, es fuera del modo como se ofrece y reflejada en sí o tiene en sí misma una verdad opuesta."""
    },
    {
        "id": "p06",
        "pagina": 78,
        "texto": """...es para ella todo este movimiento que antes se distribuía entre el objeto y la conciencia. La cosa es un uno, reflejado en sí; es para sí, pero es también para otro; y es tanto un otro para sí como ella es para otro. La cosa es, según esto, para sí y también un uno, aunque el ser uno contradiga a esta su diversidad; la conciencia debiera, por tanto, asumir de nuevo esta unificación, manteniéndola alejada de la cosa. Debiera, por consiguiente, decir que la cosa, en tanto es para sí, no es para otro. Sin embargo, es a la cosa misma a la que corresponde el ser uno, como la conciencia ha experimentado; la cosa se ha reflejado esencialmente en sí. El también o la diferencia indiferente cae, evidentemente en la cosa lo mismo que el ser uno, pero puesto que se trata de momentos diversos, no caen en la misma cosa, sino en cosas distintas; la contradicción, que es en la esencia objetiva en general, se distribuye entre dos objetos. La cosa es, por tanto, indudablemente, en y para sí, igual a sí misma, pero esta unidad consigo misma se ve perturbada por otras cosas; así se mantiene la unidad de la cosa y, al mismo tiempo, el ser otro tanto fuera de ella como fuera de la conciencia.

Ahora bien, aunque la contradicción de la esencia objetiva se distribuyó, así, entre distintas cosas, no por ello dejará de darse la diferencia dentro de la cosa singular y separada. Por tanto, las distintas cosas son puestas para sí, y la pugna cae mutuamente entre ellas de tal modo, que cada cual no se diferencia de sí misma, sino solamente de la otra. Pero cada cosa se determina ella misma como algo diferente y tiene en ella la diferencia esencial con respecto a otras, pero al mismo tiempo no de tal modo que esta contraposición se dé en ella misma, sino de modo que es para sí una determinabilidad simple, que constituye su carácter esencial, que la distingue de otras. Pero, de hecho, puesto que la diversidad se halla en la cosa, es en ella, necesariamente, como diferencia real de múltiple constitución. Sin embargo, como la determinabilidad constituye la esencia de la cosa, por medio de la cual ésta se distingue de otras y es para sí, tenemos que esta constitución diversa y múltiple es lo no esencial. Por tanto, la cosa tiene, evidentemente, en su unidad un doble en tanto que, pero con valores desiguales, lo que hace que este ser contrapuesto no llegue a ser la contraposición real de la cosa misma; sino que en cuanto la cosa se pone en contraposición a través de su diferencia absoluta, sólo se contrapone a otra cosa fuera de ella. La multiplicidad diversa, sin embargo, se da también necesariamente en la cosa, de tal modo que no es posible eliminarla de ella, pero le es algo no esencial.

Esta determinabilidad, que constituye el carácter esencial de la cosa y la distingue de todas las otras se determina ahora de modo..."""
    },
    {
        "id": "p07",
        "pagina": 79,
        "texto": """...que la cosa se halla así en contraposición a las otras, pero debe mantenerse en ello para sí. Ahora bien, es cosa o lo uno que es para sí sólo en cuanto no se halla en esta relación con otras, pues en esta relación se pone más bien la conexión con lo otro, y la conexión con lo otro es el cesar del ser para sí. Es precisamente por medio de su carácter absoluto y de su contraposición como la cosa se comporta ante las otras y sólo es esencialmente, este comportarse; pero el comportarse es la negación de su independencia, y la cosa se derrumba más bien por medio de su propiedad esencial.

La necesidad para la conciencia de la experiencia de que la cosa se derrumba precisamente a través de la determinabilidad, que constituye su esencia y su ser para sí, puede resumirse, ateniéndose al concepto simple, en los siguientes términos. La cosa se pone como ser para sí o como negación absoluta de todo ser otro y, por tanto, como negación absoluta, relacionada solamente consigo; ahora bien, la negación relacionada consigo es la superación de sí misma, o el tener su esencia en un otro.

De hecho, la determinación del objeto tal como se ha manifestado no contiene nada más que esto; dicho objeto debe tener una propiedad esencial, que constituye su simple ser para sí, pero debe tener también en él mismo, en esta simplicidad, la diversidad, que aún siendo necesaria, no constituya la determinabilidad esencial. Pero ésta es una distinción que sólo reside ya en las palabras; lo no esencial, que debe ser al mismo tiempo necesario, se supera a sí mismo o es aquello que acaba de ser llamado la negación de sí mismo.

Desaparece así el último en tanto que, que separaba el ser para sí y el ser para otro; el objeto es más bien, en uno y el mismo respecto, lo contrario de sí mismo: para sí en tanto es para otro y para otro en tanto es para sí. Es para sí, reflejado en sí, un uno; pero este para sí, este ser un uno reflejado en sí se pone en unidad con su contrario, el ser para un otro, y, por tanto, sólo como superado; dicho de otro modo, este ser para sí es tan no esencial como aquello que debiera ser solamente lo no esencial, a saber: el comportarse con otro.

El objeto es superado así en sus puras determinabilidades o en las determinabilidades que debieran constituir su esencialidad, lo mismo que cuando en su ser sensible devenía algo superado. Partiendo del ser sensible, se convierte en algo universal; pero este universal, puesto que proviene de lo sensible, es esencialmente condicionado por ello mismo, y, por tanto, no es, en general, verdaderamente igual a sí mismo, sino una universalidad afectada de una contraposición, y esto explica por qué se separa en los extremos de lo singular y lo universal, del uno de las propiedades y del también de las materias..."""
    },
    {
        "id": "p08",
        "pagina": 80,
        "texto": """libres. Estas determinabilidades puras parecen expresar la esencialidad misma, pero solamente son un ser para sí, que lleva implícito el ser para otro; pero, al ser estos dos momentos esencialmente en una unidad, se presenta ahora la universalidad absoluta incondicionada y es aquí donde la conciencia entra verdaderamente por vez primera en el reino del entendimiento.

Por tanto, aunque la singularidad sensible desaparezca en el movimiento dialéctico de la certeza inmediata y devenga universalidad, ésta es sólo universalidad sensible. La apreciación ha desaparecido y el percibir toma el objeto tal y como es en sí o como algo universal en general; por consiguiente, lo singular aparece en él como verdadera singularidad, como ser en sí del uno o como ser reflejado en sí mismo. Pero es todavía un ser para sí condicionado, junto al cual aparece otro ser para sí, el de la universalidad contrapuesta a lo singular y condicionado por esto; pero estos dos extremos contradictorios no sólo aparecen contrapuestos, sino en unidad o, lo que es lo mismo, lo común a ambos, el ser para sí, lleva implícita la contraposición en general, es decir, es al mismo tiempo lo que no es un ser para sí. La sofisticadísima del percibir trata de salvar estos momentos sustrayéndolos a su contradicción y de retenerlos mediante la separación de los puntos de vista, mediante el también y el en tanto que, y, por último, de captar lo verdadero por medio de la distinción de lo no esencial y de una esencia contrapuesta a ello. Sin embargo, estos recursos, en vez de cerrar el paso a la ilusión en el aprehender, se muestran por sí mismos como nulos; y lo verdadero, que debe ser ganado mediante esta lógica del percibir, resulta desde uno y el mismo punto de vista lo contrario y tiene como su esencia la universalidad carente de toda distinción y determinación.

Estas abstracciones vacías de la singularidad y de la universalidad contrapuesta a ella, así como de la esencia enlazada a un algo no esencial y de un algo no esencial que es, al mismo tiempo, sin embargo, necesario, son las potencias cuyo juego es el entendimiento humano percipiente, que con frecuencia se llama el buen sentido; se considera como la conciencia sólida y real y sólo es, en el percibir, el juego de estas abstracciones; y donde cree ser el más rico de todos es siempre el más pobre. Arrastrado de un lado a otro por esta esencia nula, empujado de los brazos de uno a los de otro y afanándose por afirmar, bajo la acción de esa sofisticadísima, alternativamente lo uno y lo contrario, resistiéndose a la verdad, supone que la filosofía se limita a tratar de las cosas del pensamiento. Y es cierto que trata también de ellas y las reconoce como las esencias puras, como elementos y potencias absolutos; pero, con ellos, las reconoce al mismo tiempo en su determinabilidad, y de este modo, las domina, mientras que aquel entendimiento percipiente las capta como lo verdadero y se ve empujado por ellas de error en error."""
    },
    {
        "id": "p09",
        "pagina": 81,
        "texto": """El mismo conocimiento percipiente no llega a la conciencia de que las que en él rigen son esas simples esencialidades y supone manejar siempre materias y contenidos perfectamente sólidos, del mismo modo que la certeza sensible ignora que su esencia es la abstracción vacía del ser puro; pero, de hecho, el entendimiento a que nos referimos va y viene a través de toda la materia y todo el contenido apoyándose en estos elementos, que lo mantienen en cohesión y le dan su posición dominante, y ellos solamente son lo que hace de lo sensible la esencia para la conciencia, lo que determina su comportamiento hacia ella y en lo que discurre el movimiento del percibir y de lo verdadero para él. Este curso, una determinación constantemente cambiante de lo verdadero y la superación de esta determinación, es lo que en rigor constituye la vida y la acción diaria y constante de la conciencia percipiente y que supone moverse en la verdad. Por este camino, dicha conciencia marcha inconteniblemente hacia el resultado de la misma superación de todas estas esencialidades o determinaciones esenciales, pero en cada momento singular sólo tiene conciencia de una de estas determinabilidades como lo verdadero, para pasarse en seguida a la opuesta. Tal parece como si barruntase su no esencialidad; para salvarlas del peligro que las amenaza, recurre a la sofisticuella afirmando ahora como lo verdadero lo que hace apenas un momento afirmaba como lo no verdadero. A lo que la naturaleza de estas esencias no verdaderas quiere, en rigor, empujar a este entendimiento es a agrupar los pensamientos de aquella universalidad y singularidad, del también y del uno, de aquella esencialidad necesariamente enlazada a una no esencialidad y de algo no esencial que es sin embargo necesario, los pensamientos de estas no-essencias, superándolos así; en cambio, el entendimiento a que nos referimos trata de resistir, apoyándose para ello en el en tanto que y en los distintos puntos de vista o recurriendo a asumir uno de los pensamientos para mantener el otro separado y como lo verdadero. Pero la naturaleza de estas abstracciones las agrupa en y para sí, y el buen sentido es presa de esos pensamientos, que lo arrastran en su torbellino. Trata de infundirlos el carácter de la verdad asumiendo unas veces la no-verdad de ellas y otras veces llamando a la ilusión una apariencia nacida de la inseguridad de las cosas, separando lo esencial de algo que les es necesario y que, sin embargo, debe ser no esencial, y reteniendo aquello frente a esto como su verdad, pero, al proceder de este modo, no mantiene en ellos su verdad y se da a sí, la no-verdad."""
    }
]

# Notas de análisis del Capítulo II
NOTAS_PERCEPCION = {
    "p01": "Fragmento p01 (p71): Introducción a la percepción, principio de universalidad, distinción objeto/percibir, anuncio de la cosa con múltiples cualidades.",
    "p02": "Fragmento p02 (p72): Concepto de la cosa; superación del esto en propiedad; ejemplo de la sal; el 'también' como unidad formal.",
    "p03": "Fragmento p03 (p74): Desarrollo de la cosa como uno y también; momentos de la cosa (universalidad pasiva, negación, multiplicidad).",
    "p04": "Fragmento p04 (p74): La percepción contradictoria; la conciencia como pura aprehensión; posibilidad de ilusión; oscilación entre uno y comunidad; reflexión de la conciencia.",
    "p05": "Fragmento p05 (p76): La conciencia atribuye la multiplicidad a sus sentidos; la cosa como uno; pero la propiedad esencial implica oposición; el 'en tanto que' como recurso.",
    "p06": "Fragmento p06 (p78): La contradicción se distribuye entre cosas; intento de salvar la unidad mediante lo esencial vs. accidental; fracaso.",
    "p07": "Fragmento p07 (p79): Culminación de la percepción. La cosa se derrumba por su propiedad esencial; desaparición del 'en tanto que'; coincidencia de ser para sí y ser para otro; surgimiento de la universalidad afectada de contraposición.",
    "p08": "Fragmento p08 (p80): La universalidad incondicionada; el reino del entendimiento; crítica al entendimiento percipiente (buen sentido).",
    "p09": "Fragmento p09 (p81): Conclusión: el entendimiento percipiente es presa de abstracciones; necesidad de superarlas."
}

# Ejemplos concretos del Capítulo II
EJEMPLOS_PERCEPCION = {
    "p02": [{"tipo": "sal", "propiedades": ["blanca", "salina", "cúbica", "peso determinado"], "unidad": "aquí simple", "contradiccion": "una y múltiple a la vez"}],
    "p07": [{"tipo": "contradicción de la propiedad esencial", "descripcion": "cualquier cosa, al ser definida por una propiedad esencial, se relaciona necesariamente con lo otro y se derrumba", "ejemplo": "la sal es salina solo en oposición a lo dulce; su ser para sí es ser para otro"}]
}

# Momentos dialécticos del Capítulo II
MOMENTOS_PERCEPCION = [
    "transición desde certeza sensible",
    "establecimiento del principio de universalidad",
    "distinción objeto (esencia) / percibir (inesencial)",
    "anuncio de la cosa con múltiples cualidades",
    "superación del esto en propiedad",
    "la propiedad como universal determinado",
    "multiplicidad de propiedades indiferentes",
    "la cosa como médium de coexistencia",
    "el 'también' como unidad formal",
    "ejemplo de la sal",
    "desarrollo de la cosa como uno y también",
    "momentos de la cosa: universalidad pasiva, negación, multiplicidad",
    "conciencia como pura aprehensión",
    "posibilidad de ilusión",
    "criterio de igualdad consigo misma",
    "objeto como uno",
    "propiedad universal rebasa singularidad",
    "propiedad determinada excluyente",
    "oscilación entre uno y comunidad",
    "intento de captar propiedad singular aislada (fracaso)",
    "retorno al ciclo de la percepción",
    "reflexión de la conciencia",
    "distinción entre aprehensión y no-verdad",
    "corrección consciente",
    "conciencia de la reflexión",
    "la conciencia atribuye la multiplicidad a sus sentidos",
    "la cosa como uno y también",
    "el 'en tanto que' como recurso",
    "la cosa como suma de materias",
    "la cosa se muestra de doble modo",
    "la cosa como uno reflejado en sí y para otro",
    "distribución de la contradicción entre cosas",
    "determinabilidad esencial vs. multiplicidad accidental",
    "fracaso de la distinción esencial/accidental",
    "la cosa como unidad irresoluble de opuestos",
    "anuncio del tránsito al entendimiento",
    "la cosa se derrumba por su propiedad esencial",
    "la negación absoluta se supera a sí misma",
    "desaparición del 'en tanto que'",
    "coincidencia de ser para sí y ser para otro",
    "el objeto se supera en sus determinabilidades",
    "surgimiento de la universalidad afectada de contraposición",
    "separación en extremos (singular/universal, uno/también)",
    "transición inminente al entendimiento",
    "universalidad incondicionada",
    "reino del entendimiento",
    "crítica al entendimiento percipiente (buen sentido)",
    "abstracciones vacías",
    "el entendimiento percipiente como juego de abstracciones",
    "superación de las no-esencias"
]

# Metáforas clave del Capítulo II
METAFORAS_PERCEPCION = [
    "cosa", "cualidades", "universal", "multiplicidad", "negación", "percepción",
    "ilusión", "movimiento", "despliegue", "reunión", "simple", "esencial", "no esencial",
    "sal", "blanca", "salino", "cúbica", "peso", "también", "cosidad", "médium", "coexistencia", "superación",
    "uno", "excluyente", "universalidad sensible", "propiedad", "materias", "ser para sí", "ser para otro",
    "en tanto que", "punto de vista", "buen sentido", "abstracciones vacías", "esencias puras", "potencias",
    "derrumbarse", "negación absoluta", "superación de sí misma", "último en tanto que",
    "universalidad afectada de contraposición", "extremos", "uno de las propiedades", "también de las materias",
    "reino del entendimiento", "juego de abstracciones", "no-esencias", "torbellino"
]


# -------------------------------------------------------------------
# DATOS DEL CAPÍTULO III (FRAGMENTOS)
# -------------------------------------------------------------------

FRAGMENTOS_CAPITULO3 = [
    {
        "id": "e01",
        "pagina": 82,
        "texto": """III. FUERZA Y ENTENDIMIENTO, FENÓMENO Y MUNDO SUPRASENSIBLE

En la dialéctica de la certeza sensible han desaparecido en el pasado, para la conciencia, el oído, la visión, etc., y como percepción la conciencia ha arribado a pensamientos que, no obstante, agrupa primeramente en lo universal incondicionado. Ahora bien, este algo incondicionado, si se lo tomase como simple esencia quieta, no sería, a su vez, más que el extremo del ser para sí puesto de un lado, pues frente a él aparecería la no-esencia, pero referido a ésta él mismo sería algo no esencial y la conciencia no saldría de la ilusión del percibir; sin embargo, ha resultado ser algo que ha retornado a sí, particularmente en el sentido del oído. Este universal incondicionado que es a partir de ahora el verdadero objeto de la conciencia sigue siendo objeto de ella; aún no ha captado su concepto como concepto. Hay que establecer una distinción esencial entre ambas cosas; para la conciencia, el objeto ha retornado a sí desde el comportamiento hacia otro, y con ello ha devenido concepto en sí; pero la conciencia no es todavía para sí misma el concepto, por lo cual no se reconoce en aquel objeto reflejado. Este objeto deviene para nosotros a través del movimiento de la conciencia de tal modo que la conciencia se ha entrelazado con este devenir y la reflexión es en ambos lados la misma o solamente una. Pero, como la conciencia, en este movimiento, tendría como contenido solamente la esencia objetiva, y no la conciencia como tal, tenemos que para ella hay que poner el resultado en una significación objetiva y la conciencia como lo que se refleja de lo que ha devenido, de modo que esto es para ella, como lo objetivo, la esencia.

El entendimiento ha superado así, evidentemente, su propia no-verdad y la no-verdad del objeto; y resultado de ello es para él el concepto de lo verdadero, como verdadero que es en sí y que aún no es concepto o que carece del ser para sí de la conciencia; algo verdadero que el entendimiento deja hacer sin subirse en él. Este algo verdadero impulsa su esencia para sí misma; de tal modo que la conciencia no participa para nada en su libre realización [Realisierung], sino que se limita a contemplarla y la aprehende, puramente. Lo que nosotros, según esto, tenemos que hacer, ante todo, es ponernos en su lugar y ser el concepto que plasma lo que se contiene en el resultado; es en este objeto plasmado, que se presenta"""
    },
    {
        "id": "e02",
        "pagina": 83,
        "texto": """ante la conciencia como algo que es, donde la conciencia deviene ante sí misma conciencia consciente.

El resultado era lo universal incondicionado, primeramente en el sentido negativo y abstracto de que la conciencia negaba sus conceptos unilaterales y los convertía en algo abstracto, es decir, los abandonaba. Pero el resultado tiene en sí la significación positiva de que en él se pone de un modo inmediato como la misma esencia la unidad del ser para sí y del ser para otro o la contraposición absoluta. Por ahora, esto sólo parece afectar a la forma de los momentos, el uno con respecto al otro; pero el ser para sí y el ser para otro es igualmente el contenido mismo, puesto que la contraposición no puede tener en su verdad más naturaleza que la que se ha mostrado en el resultado, a saber: la de que el contenido tenido por verdadero en la percepción sólo pertenece de hecho a la forma y se disuelve en su unidad. Y este contenido es al mismo tiempo universal; no puede haber allí ningún otro contenido que por su especial constitución se sustraiga al retorno a esta universalidad incondicionada. Semejante contenido sería un modo determinado cualquiera de ser para sí y de comportarse hacia otro. Sin embargo, ser para sí y comportarse hacia otro en general constituyen la naturaleza y la esencia de un contenido cuya verdad es la de ser universal incondicionado; y el resultado es pura y simplemente universal.

Ahora bien, como este universal incondicionado es objeto para la conciencia, se manifiesta en él la diferencia entre la forma y el contenido, y en la figura del contenido los momentos tienen el aspecto en el que primeramente se ofrecían: de una parte, el de médium universal de múltiples materias subsistentes y, de otra parte, el de uno reflejado en sí, en el que queda aniquilada su independencia. Aquél es la disolución de la independencia de la cosa o la pasividad, que es un ser para otro; éste, empero, el ser para sí. Hay que ver cómo estos momentos se presentan en la universalidad incondicionada, que es su esencia. Se comprende claramente, ante todo, que dichos momentos, por el hecho de que sólo tienen su ser en esta universalidad, no pueden ya en general mantenerse el uno aparte del otro, sino que son, esencialmente, lados que se superan en ellas mismos y sólo se pone el tránsito del uno al otro.

---

## [1. La fuerza y el juego de las fuerzas]

Uno de los momentos se presenta, pues, como la esencia dejada a un lado, como médium universal o como la subsistencia de materias independientes. Pero la independencia de estas materias no es..."""
    },
    {
        "id": "e03",
        "pagina": 85,
        "texto": """...sino este médium; o bien, este universal es totalmente la multiplicidad de aquellos diversos universales. Pero el que lo universal forme en él mismo una unidad inseparable con esta multiplicidad significa que estas materias son cada una de ellas donde la otra es; se penetran mutuamente, pero sin tocarse, ya que, a la inversa, la multiplicidad diferenciada es igualmente independiente. Con lo cual se establece también su pura porosidad o su ser superadas. Y, a su vez, este ser superados o la reducción de esta diversidad al puro ser para sí no es otra cosa que el médium mismo, y éste la independencia de las diferencias. Dicho de otro modo: las diferencias establecidas como independientes pasan de modo inmediato a su unidad; ésta pasa a ser también de modo inmediato el despliegue, y el despliegue retorna, a su vez, a la reducción. Este movimiento es lo que se llama fuerza: uno de los momentos de ella, o sea la fuerza en cuanto expansión de las materias independientes en su ser, es su exteriorización; pero la fuerza como el desaparecer de dichas materias es la fuerza que desde su exteriorización se ve repelida de nuevo hacia sí, o la fuerza propiamente dicha. Pero, en primer lugar, la fuerza replegada sobre sí misma necesita exteriorizarse; y, en segundo lugar, en la exteriorización, la fuerza es una fuerza que es en sí misma, del mismo modo que en este ser en sí misma es exteriorización. Al obtener así ambos momentos en su unidad inmediata, el entendimiento, al que pertenece el concepto de fuerza, es propiamente el concepto que lleva en sí los momentos diferentes, como diferentes, ya que deben ser distintos en la fuerza misma; la diferencia sólo es, por tanto, en el pensamiento. Dicho en otros términos: lo único que se ha establecido más arriba es el concepto de fuerza, no su realidad [Realitat]. Pero, de hecho, la fuerza es lo universal incondicionado que es en sí mismo lo que es para otro o que tiene en él mismo la diferencia, pues no es otra cosa que el ser para otro. Así, pues, para que la fuerza sea en su verdad hay que dejarla completamente libre del pensamiento y establecerla como la sustancia de estas diferencias, es decir, de una parte, como fuerza íntegra que permanece esencialmente en y para sí y, de otra parte, sus diferencias como momentos sustanciales o que subsisten para sí. La fuerza como tal o como fuerza repelida hacia sí es, según esto, para sí como un uno excluyente para el que el despliegue de las materias es otra esencia subsistente, con lo que se establecen dos lados distintos independientes. Pero la fuerza es también el todo, o sigue siendo lo que es con arreglo a su concepto; lo que vale decir que estas diferencias siguen siendo puras formas, momentos superficiales que van desapareciendo. Las diferencias entre la fuerza propiamente dicha repelida hacia sí misma..."""
    },
    {
        "id": "e04",
        "pagina": 86,
        "texto": """...ha sido todavía puesta, este otro se añade y la solicita a la reflexión en sí misma o supera su exteriorización. Pero, de hecho, ella más...

86 CONCIENCIA

...ma es este ser reflejado en sí o este ser superado de la exteriorización; el ser uno desaparece como aparecía, es decir, como un otro; la fuerza es ella misma, la fuerza repelida de nuevo hacia sí.

Lo que aparece como otro y solicita la fuerza tanto para la exteriorización como para el retorno a sí mismo es ello mismo fuerza, según el resultado inmediato, ya que lo otro es tanto como médium universal cuanto como uno y de tal modo que cada una de estas figuras aparece al mismo tiempo solamente como un momento que va desapareciendo. Según esto, la fuerza no ha salido, en general, de su concepto por el hecho de que otro es para ella y ella es para otro. Pero se dan, al mismo tiempo, dos fuerzas y, aunque el concepto de ambas sea el mismo, han pasado de su unidad a la dualidad. En vez de que la contraposición totalmente esencial sólo siguiera siendo un momento, parece como si por el desdoblamiento en fuerzas completamente independientes se sustrajera al imperio de la unidad. Qué clase de independencia es ésta, hay que examinarlo más de cerca. De momento, tenemos que la segunda fuerza aparece como la solicitante y, además, en cuanto a su contenido, como médium universal frente a la que se determina como solicitada; pero, en cuanto que aquélla es esencialmente la sucesión alternada de estos dos momentos y ella misma es fuerza, esto quiere decir que, de hecho, sólo es también el médium universal en tanto que se la solicita para serlo; en cambio, en cuanto es aquella esencial sucesión alternativa de estos dos momentos y en sí misma fuerza, es que de hecho es solamente médium universal cuando se la solicita para que lo sea, y también y del mismo modo es sólo una unidad negativa o que solicita que la fuerza sea repelida hacia sí por el hecho de ser solicitada. Y, consiguientemente, se transforma en el mismo trueque de las determinabilidades entre sí la diferencia que mediaba entre ambas y que consistía en que la una fuese la solicitante y la otra la solicitada.

El juego de las dos fuerzas subsiste, por tanto, en este contrapuesto ser determinado de ambas, en su ser la una para la otra dentro de esta determinación y del trueque absoluto e inmediato de las determinaciones, tránsito sin el cual no podrían ser estas determinaciones, en las que las fuerzas parecen presentarse de un modo independiente. La que solicita se pone, por ejemplo, como médium universal y, por el contrario, la solicitada como fuerza repelida; pero aquélla sólo es, a su vez, medium universal porque la otra es fuerza repelida; en otras palabras, ésta es más bien la solicitante con respecto a aquélla y la que la convierte en médium. Aquélla sólo adquiere su determinabilidad a través de la otra y sólo es solicitante en cuanto es solicitada por la otra para que lo sea; y vuelve a perder..."""
    },
    {
        "id": "e05",
        "pagina": 87,
        "texto": """de un modo igualmente inmediato esta determinabilidad que se le ha dado, la cual pasa a la otra o, mejor dicho, ya ha pasado; lo ajeno, lo que solicita la fuerza, aparece como médium universal, pero sólo porque la fuerza le ha solicitado que sea así; es decir, es ella la que lo pone así precisamente porque ella misma es esencialmente médium universal, pone lo que la solicita así precisamente porque esta otra determinación le es esencial, es decir, porque ella misma es más bien esta otra determinación.

Para penetrar en su totalidad en el concepto de este movimiento, podemos llamar todavía la atención hacia el hecho de que las diferencias se muestran de por sí bajo una doble diferencia: de una parte, como diferencias del contenido, en cuanto que uno de los extremos es la fuerza reflejada en sí y el otro el médium de las materias; y, de otra parte, como diferencias de la forma, en cuanto que una es la solicitante y otra la solicitada, aquélla activa y ésta pasiva. Si nos fijamos en la diferencia del contenido, vemos que los extremos son distintos en general o son distintos para nosotros; en cambio, con arreglo a la diferencia de la forma son independientes, tajantemente distintos el uno del otro en su relación, y contrapuestos. El que los extremos no son nada en sí según estos dos lados, sino que estos lados en que debería subsistir su esencia diferencial no son más que momentos que tienden a desaparecer, el paso inmediato de cada uno de los lados al lado opuesto, es algo que deviene para la conciencia en la percepción del movimiento de la fuerza. Pero, para nosotros, como ya hemos dicho, las diferencias desaparecían en sí como diferencias del contenido y de la forma, y, del lado de la forma, conforme a la esencia, lo activo, lo solicitante o lo que es para sí [era] lo mismo que del lado del contenido, como fuerza repelida hacia sí misma, y lo pasivo, lo solicitado o lo que es para otro del lado de la forma lo mismo que del lado del contenido se presentaba como médium universal de las múltiples materias.

De donde se desprende que el concepto de fuerza deviene real al desdoblarse en dos fuerzas y también cómo llega a esto. Estas dos fuerzas existen como esencias que son para sí; pero su existencia es ese movimiento de la una con respecto a la otra en cuanto su ser es más bien un puro ser puesto por un otro, es decir en cuanto su ser tiene más bien la pura significación del desaparecer. No son en cuanto extremos que hayan retenido algo fijo para sí, limitándose a transmitirse una cualidad externa el uno respecto al otro en el término medio y en su contacto, sino que lo que son lo son solamente en este término medio y contacto. Hay en ello, de un modo inmediato, tanto el ser repelido hacia sí mismo o..."""
    },
    {
        "id": "e06",
        "pagina": 88,
        "texto": """el ser para sí de la fuerza como la exteriorización, tanto el solicitar como el ser solicitado; por tanto, estos momentos no aparecen distribuidos entre dos extremos independientes que se enfrenten sólo en sus vértices contrapuestos, sino que su esencia consiste pura y simplemente en esto: en que cada uno sólo es por medio del otro y en no ser inmediatamente en tanto que el otro es. Por tanto, no tienen de hecho ninguna sustancia propia que las sostenga y mantenga. El concepto de fuerza se mantiene más bien como la esencia en su realidad misma; la fuerza como real sólo es pura y simplemente en la exteriorización, que no es, al mismo tiempo, otra cosa que un superarse a sí misma. Esta fuerza real, representada como libre de su exteriorización y como algo que es para sí, es la fuerza repelida hacia sí misma; pero esta determinabilidad es, de hecho, a su vez, como ha resultado, sólo un momento de la exteriorización. La verdad de la fuerza se mantiene, pues, solamente como el pensamiento de ella; y los momentos de su realidad, sus sustancias y su movimiento, se derrumban sin detenerse en una unidad indistinta que no es la fuerza repelida hacia sí misma (ya que ésta sólo es, a su vez, uno de tales momentos), sino que esta unidad es su concepto como concepto. La realización [Realisierung] de la fuerza es, por consiguiente, al mismo tiempo, la pérdida de la realidad [Realitat]; la fuerza ha devenido así más bien algo totalmente otro, a saber: esta universalidad que el entendimiento conoce primeramente o de un modo inmediato como su esencia y que también como su esencia se muestra en su realidad [Realitat] que debiera ser, en las sustancias reales.

### [2. Lo interior]

Si consideramos al primer universal como el concepto del entendimiento, en el que la fuerza no es todavía para sí, el segundo será ahora su esencia, tal y como se presenta en y para sí. O, a la inversa, si consideramos el primer universal como lo inmediato, que debiera ser un objeto real para la conciencia, tenemos que el segundo se halla determinado como lo negativo de la fuerza sensible objetiva; es la fuerza tal y como es en su verdadera esencia, solamente en cuanto objeto del entendimiento; aquel primero sería la fuerza repelida hacia sí misma o la fuerza como sustancia; este segundo, en cambio, lo interior de las cosas como interior, que es lo mismo que el concepto como concepto.

(a) El mundo suprasensible

[1. Lo interior, el fenómeno, el entendimiento] Esta esencia, ver-"""
    },
    {
        "id": "e07",
        "pagina": 89,
        "texto": """FUERZA Y ENTENDIMIENTO

dada de las cosas se ha determinado ahora de tal modo que no es inmediatamente para la conciencia, sino que ésta mantiene un comportamiento mediato hacia lo interior y, como entendimiento, contempla, a través de este término medio del juego de las fuerzas, al fondo verdadero de las cosas. El término medio que enlaza los dos extremos, el entendimiento y lo interior, es el ser desarrollado de la fuerza, que de ahora en adelante es para el entendimiento mismo un desaparecer. Por eso se le da el nombre de manifestación [Erscheinung], ya que llamamos apariencia [Schein] al ser que es en él mismo, de modo inmediato, un no-ser. Pero no es solamente una apariencia sino un fenómeno, la totalidad de lo que aparece. Esta totalidad, como totalidad o lo universal, es lo que constituye lo interior, el juego de fuerzas, como reflexión de ese juego en sí mismo. En él, las esencias de la percepción son puestas para la conciencia de un modo objetivo tal y como son en sí, es decir, como momentos que sin descanso ni ser se truecan de un modo inmediato en lo contrario, lo uno inmediatamente en lo universal, lo esencial inmediatamente en lo no esencial, y a la inversa. Este juego de fuerzas es, por tanto, lo negativo desarrollado; pero la verdad de él es lo positivo, a saber: lo universal, el objeto que es en sí. El ser del mismo para la conciencia es mediado por el movimiento de la manifestación, en el que el ser de la percepción y lo objetivo sensible en general tiene solamente una significación negativa y la conciencia, por tanto, se refleja en sí, partiendo de ello, como en lo verdadero, pero como conciencia vuelve a convertir este algo verdadero en interior objetivo, distinguiendo esta reflexión de las cosas de su reflexión en sí misma, del mismo modo que el movimiento mediador sigue siendo para ella algo objetivo. Este interior es, por tanto, para la conciencia, un extremo frente a ella; pero es también, para ella, lo verdadero, puesto que en ello tiene, al mismo tiempo, como en el en sí, la certeza de sí mismo o el momento de su ser para sí; sin embargo, no es aún consciente de este fundamento, ya que el ser para sí que lo interior debería tener en él mismo no sería otra cosa que el movimiento negativo; pero, para la conciencia, este movimiento negativo sigue siendo el fenómeno objetivo que va desapareciendo y no es todavía su propio ser para sí; lo interior es, para él, por tanto, concepto, pero la conciencia no conoce aún la naturaleza del concepto.

En este verdadero interior, como lo universal absoluto depurado de la contraposición de lo universal y lo singular y devenido para el entendimiento, se revela ahora por vez primera, más allá del mundo sensible como el mundo que se manifiesta, un mundo suprasensible como el mundo verdadero, por encima del más acá llamado a desapa-"""
    },
    {
        "id": "e08",
        "pagina": 90,
        "texto": """recer el más allá permanente; un en sí que es la manifestación primera de la razón, manifestación todavía, por tanto, imperfecta o solamente el puro elemento en que la verdad tiene su esencia.

Nuestro objeto será, por tanto, en lo sucesivo, el silogismo que tiene como extremos el interior de las cosas y el entendimiento y como término medio el fenómeno; pero el movimiento de este silogismo suministra la ulterior determinación de lo que el entendimiento contempla en el interior a través de aquel término medio y la experiencia que hace acerca de este comportarse de lo enlazado por el razonamiento.

[2. Lo suprasensible, como manifestación] Lo interior sigue siendo un puro más allá para la conciencia, ya que ésta no se encuentra aún por sí misma en él; es vacío, pues es solamente la nada del fenómeno y, positivamente, es lo universal simple. Este modo de ser de lo interior asiente de un modo inmediato a quienes dicen que el interior de las cosas es incognoscible; pero el fundamento de esto debiera captarse de otro modo. De este algo interior tal y como es aquí de un modo inmediato no se da, evidentemente, conocimiento alguno, pero no porque la razón sea para ello demasiado corta de vista, limitada, o como quiera llamársela, acerca de lo cual aún no sabemos nada, por ahora, pues no hemos penetrado tan a fondo; sino por virtud de la simple naturaleza de la cosa misma, a saber: porque en lo vacío no se conoce nada o, expresando lo mismo del otro lado, porque se lo determina precisamente como el más allá de la conciencia. El resultado es, evidentemente, el mismo si se sitúa a un ciego en medio de la riqueza del mundo suprasensible —suponiendo que este mundo tenga tal riqueza, ya se trate del contenido peculiar de este mundo o ya sea la conciencia misma este contenido— que si se coloca a un hombre que ve en medio de las puras tinieblas o, si se quiere, en la pura luz, suponiendo que el mundo suprasensible sea esto; el hombre dotado de visión no verá ni bajo la pura luz ni en medio de las puras tinieblas, lo mismo que el ciego no alcanzaría a ver nada de la plétora de riquezas desplegadas ante él. Si no se pudiera hacer nada con lo interior y el entrelazamiento con él mediante el fenómeno, no quedaría más camino que atenerse al fenómeno mismo, es decir, tomar como verdadero algo de lo que sabemos que no lo es; o bien, para que en este vacío, devenido primeramente como vaciedad de cosas objetivas, pero que luego, como vaciedad en sí, debe tomarse como vacío de todos los comportamientos espirituales y diferencias de la conciencia como conciencia, para que en este vacío total a que se da también el nom-"""
    },
    {
        "id": "e09",
        "pagina": 91,
        "texto": """bre de lo sagrado, haya algo, por lo menos, lo llenamos de sueños, de fenómenos que la conciencia misma engendra; y tendría que contentarse con recibir ese trato, no siendo digno de otro mejor, ya que, después de todo, los mismos sueños son preferibles a su vaciedad.

Pero lo interior o el más allá suprasensible ha nacido, proviene de la manifestación y ésta es su mediación; en otros términos, la manifestación es su esencia y es, de hecho, lo que la llena. Lo suprasensible es lo sensible y lo percibido, puestos como en verdad lo son; y la verdad de lo sensible y lo percibido es, empero, ser fenómeno. Lo suprasensible es, por tanto, el fenómeno como fenómeno. Si se pensara que lo suprasensible es, por tanto, el mundo sensible o el mundo tal y como es para la certeza y la percepción sensibles inmediatas, lo entenderíamos al revés, pues el fenómeno más bien no es el mundo del saber y la percepción sensibles como lo que son, sino puestos como superados o en verdad como interiores. Suele decirse que lo suprasensible no es la manifestación; pero, al decir esto, no se entiende por manifestación la manifestación, sino más bien el mundo sensible mismo, como realidad real [reelle Wirklichkeit].

[3. La ley como la verdad de la manifestación] El entendimiento, que es nuestro objeto, se halla cabalmente en el lugar en que para él lo interior ha devenido en sí solamente en cuanto lo universal todavía no lleno; el juego de fuerzas sólo tiene, cabalmente, esta significación negativa de no ser en sí y la positiva de ser lo medidor, pero fuera del entendimiento. Pero su relación con lo interior se llenará para el entendimiento. El juego de fuerzas es algo inmediato para el entendimiento, pero lo verdadero es para él lo interior simple; el movimiento de la fuerza sólo es, por tanto, asimismo, lo verdadero como lo simple en general. Ahora bien, por lo que a este juego de fuerzas se refiere, hemos visto que, según su constitución, la fuerza solicitada por otra es, al mismo tiempo, la solicitante con respecto a ésta, la cual se convierte en solicitante, a su vez y por ello mismo. Aquí sólo se da el trueque inmediato o la mutación absoluta de la determinabilidad, que constituye el único contenido de lo que aparece; el ser o bien médium universal o bien unidad negativa. Lo que aparece de un modo determinado deja de ser inmediatamente lo que es al aparecer; mediante este modo determinado de aparecer solicita al otro lado, que así se exterioriza; es decir, este otro lado es inmediatamente, ahora, lo que el primero debiera ser. Estos dos lados, el comportamiento del solicitar y el comportamiento del contenido determinado opuesto, son cada uno para sí la inversión y el trueque absolutos. Pero estos dos comportamientos son, a su vez,..."""
    },
    {
        "id": "e10",
        "pagina": 92,
        "texto": """92 CONCIENCIA

uno y el mismo; y la diferencia de la forma, el ser lo solicitado y lo solicitante, es lo mismo que la diferencia del contenido, lo solicitado en cuanto tal, a saber; el medium pasivo, y lo solicitante, en cambio, el médium activo, la unidad negativa o lo uno. Desaparece con ello toda diferencia entre las fuerzas particulares que, la una frente a la otra, debieran darse en general en este movimiento, ya que se basaban exclusivamente en aquella diferencia; y la diferencia entre las fuerzas forma, a su vez, una unidad con ambas. Aquí no se da ya, pues, ni la fuerza ni el solicitar y el ser solicitado, ni la determinabilidad de ser médium subsistente y unidad reflejada en sí, ni algo singular para sí ni diversas contraposiciones; en este cambio absoluto sólo se da ya la diferencia como universal o como la diferencia a que han quedado reducidas las múltiples contraposiciones. Esta diferencia como universal es, por tanto, lo simple en el juego de la fuerza misma y lo verdadero de él; es la ley de la fuerza.

A través de su relación con la simplicidad de lo interior o del entendimiento, la manifestación absoluta cambiante se convierte en la diferencia simple. Lo interior, primeramente, sólo es lo universal en sí; este simple universal en sí es, sin embargo, esencialmente, de un modo no menos absoluto, la diferencia universal, pues es el resultado del cambio mismo, o el cambio es su esencia; pero el cambio, como puesto en lo interior, como en verdad es, es acogido en este interior como diferencia asimismo absolutamente universal, aquietada, que permanece igual a sí. En otras palabras, la negación es momento esencial de lo universal y ella o la mediación son, por tanto, en lo universal, diferencia universal. Dicha diferencia se expresa en la ley como la imagen constante del fenómeno inestable. El mundo suprasensible es, de este modo, un tranquilo reino de leyes, ciertamente más allá del mundo percibido, ya que este mundo sólo presenta la ley a través del constante cambio, pero las leyes se hallan precisamente presentes en él, como su tranquila imagen inmediata.

[β] La ley, como diferencia y homonimia]

[1. Las leyes determinadas y la ley universal] Este reino de las leyes es, ciertamente, la verdad del entendimiento, que tiene su contenido en la diferencia que es en la ley; pero, al mismo tiempo, sólo es su primera verdad y no agota totalmente la manifestación. La ley se halla presente en él, pero no es toda su presencia; bajo circunstancias sin cesar distintas, tiene una realidad siempre otra. Esto hace que la manifestación para sí tenga un lado que no es en lo interior; en otros términos, la manifestación no aparece pues-"""
    },
    {
        "id": "e11",
        "pagina": 93,
        "texto": """ta todavía en verdad como manifestación, como ser para sí superado. Y este defecto de la ley necesariamente tiene que manifestarse también en la ley misma. Lo que parece faltarle es que, aun teniendo en sí misma la diferencia, sólo la tiene como diferencia universal, indeterminada. Pero, en cuanto que no es la ley en general, sino una ley, tiene en ella la determinabilidad, con lo cual se da una multiplicidad indeterminada de leyes. Sin embargo, esta multiplicidad es más bien, ella misma, un defecto, pues contradice al principio del entendimiento para el que, como conciencia de lo interior simple, lo verdadero es la unidad universal en sí. De ahí que tenga que hacer coincidir más bien las múltiples leyes en una sola ley, por ejemplo en la ley según la cual la piedra cae o en la que rige el movimiento de las esferas celestes concebidas como una sola ley. Pero, en esta coincidencia, las leyes pierden su determinabilidad; la ley se torna cada vez más superficial, con lo que se encuentra, de hecho no la unidad de estas leyes determinadas, sino una ley que elimina su determinabilidad; como la ley única que agrupa en sí las leyes de la caída de los cuerpos en la tierra y la del movimiento celeste no expresa en realidad las dos. La unificación de todas las leyes en la atracción universal no expresa más contenido que el mero concepto de la ley misma, que aquí se pone como algo que es. La atracción universal nos dice que todo tiene una diferencia constante con lo otro. El entendimiento supone haber descubierto aquí una ley universal que expresa la realidad universal como tal, pero sólo ha descubierto, de hecho, el concepto de la ley misma, algo así como si declarara que toda realidad es en ella misma conforme a ley. La expresión de la atracción universal tiene, por tanto, gran importancia en cuanto que va dirigida contra esa representación carente de pensamiento para la que todo se presenta bajo la figura de lo contingente y según la cual la determinabilidad tiene la forma de la independencia sensible.

La atracción universal o el concepto puro de la ley se enfrentan, así, a las leyes determinadas. En cuanto este concepto puro se considera como la esencia o como lo interior verdadero, la determinabilidad de la ley determinada misma sigue perteneciendo al fenómeno o más bien al ser sensible. Sin embargo, el concepto puro de la ley no sólo va más allá de la ley, la cual, como ley determinada, se enfrenta a otras leyes determinadas, sino que va también más allá de la ley como tal. La determinabilidad de que se hablaba sólo es en sí misma, propiamente, un momento que tiende a desaparecer y que aquí no puede ya presentarse como esencialidad, pues sólo se da la ley como lo verdadero, pero el concepto de ley se vuelve contra la ley misma..."""
    },
    {
        "id": "e12",
        "pagina": 94,
        "texto": """misma. Y en la ley precisamente se aprehende la diferencia misma de un modo inmediato y se acoge en lo universal, con lo cual subsisten los momentos cuya relación expresa la ley como esencialidades indiferentes y que son en sí. Pero estas partes de la diferencia en la ley son sin embargo, al mismo tiempo, lados a su vez determinados; el concepto puro de la ley como atracción universal, en su verdadera significación, debe aprehenderse de tal modo que en él, como en lo absolutamente simple, las diferencias que se dan en la ley como tal retornen de nuevo a lo interior como unidad simple; esta unidad es la necesidad interna de la ley.

[2. Ley y fuerza] La ley se presenta, pues, de dos modos, de una parte como ley en la que las diferencias se expresan como momentos independientes; de otra parte, en la forma del simple ser retornado a sí mismo, que a su vez puede llamarse fuerza, pero de tal modo que no se entiende por tal fuerza repelida hacia sí misma, sino la fuerza en general o el concepto de la fuerza, es decir, una abstracción que atrae hacia sí las diferencias entre lo que es atraído y lo que atrae. Así, por ejemplo, la electricidad simple es la fuerza; pero la expresión de la diferencia corresponde a la ley; esta diferencia es la electricidad positiva y la negativa. En el movimiento de caída, la fuerza es lo simple, la gravedad, que responde a la ley según la cual las magnitudes de los momentos diferentes del movimiento, el tiempo transcurrido y el espacio recorrido, se comportan entre sí como la raíz y el cuadrado. La electricidad misma no es la diferencia en sí o, en su esencia, no es la doble esencia de la electricidad positiva y negativa; por eso suele decirse que tiene la ley de ser de ese modo y también que tiene la propiedad de exteriorizarse así. Esta propiedad es, ciertamente, esencial y la única propiedad de esta fuerza o le es necesaria. Pero la necesidad es, aquí, una palabra vacua; la fuerza debe desdoblarse así sencillamente porque debe. Claro está, que, si se pone la electricidad positiva, también la negativa en sí es necesaria, ya que lo positivo sólo es como relación a algo negativo, o lo positivo es en él mismo la diferencia de sí mismo, ni más ni menos que lo negativo. Pero el que la electricidad en cuanto tal se divida así no es en sí lo necesario; como simple fuerza, la electricidad es indiferente con respecto a su ley de ser como positiva y negativa; y si llamamos a lo necesario, su concepto y a esto, a la ley, empero, su ser, entonces su concepto es indiferente con respecto a su ser; la electricidad sólo tiene esta propiedad; lo que cabalmente significa que ella no le es en sí necesaria. Esta indiferencia se presenta bajo otra forma cuando se dice que de la definición de la electricidad forma parte el ser como positiva y..."""
    },
    {
        "id": "e13",
        "pagina": 95,
        "texto": """negativa o que esto es sencillamente su concepto y esencia. Su ser significaría entonces su existencia en general; pero en aquella definición no va implícita la necesidad de su existencia; ésta es o porque se la encuentra, lo que significa que no es para nada necesaria, o bien responde a otras fuerzas, es decir, su necesidad es externa. Pero al situar la necesidad en la determinabilidad del ser por medio de otro recaemos de nuevo en la multiplicidad de las leyes determinadas, que habíamos abandonado para considerar la ley como ley; con ésta solamente hay que cotejar su concepto como concepto o su necesidad, que en todas estas formas se había mostrado, sin embargo, ante nosotros solamente como una palabra vacua.

La indiferencia de la ley y de la fuerza o del concepto y del ser se presenta, además, de otro modo, distinto del que acabamos de indicar. Por ejemplo, en la ley del movimiento es necesario que éste se divida en tiempo y espacio o también en distancia y velocidad. Al ser solamente la relación entre aquellos momentos, el movimiento, es lo universal, aquí, evidentemente, dividido en sí mismo; pero estas partes, tiempo y espacio, o distancia y velocidad, no expresan en ellas este origen de lo uno; son indiferentes entre sí, el espacio es representado como si pudiera ser sin el tiempo, el tiempo sin el espacio y la distancia, al menos, sin la velocidad, del mismo modo que son indiferentes entre sí sus magnitudes, puesto que no se comportan como lo positivo y lo negativo ni se relacionan, por tanto, las unas con las otras por su esencia. La necesidad de la división se presenta, pues, aquí, pero no la de las partes como tales, la una con respecto a la otra. Lo que quiere decir, empero, que aquella primera necesidad no pasa de ser una falsa necesidad disfrazada de tal; en efecto, el movimiento no es representado él mismo como simple o como pura esencia, sino ya como dividido; tiempo y espacio son sus partes independientes o esencias en ellas mismas, o distancia y velocidad modos del ser o del representarse cada uno de los cuales puede ser sin el otro, por lo que el movimiento sólo es su relación superficial, pero no su esencia. Representado como simple esencia o como fuerza, el movimiento es, ciertamente, la gravedad, la cual, sin embargo, no encierra en ella para nada estas diferencias.

[3. La explicación] En ninguno de los dos casos es la diferencia, por tanto, una diferencia en sí misma; o bien lo universal, la fuerza, es indiferencia con respecto a la división que es en la ley, o bien las diferencias, las partes de la ley, son indiferentes las unas con respecto a las otras. Pero el entendimiento tiene el concepto de esta diferencia en sí, cabalmente porque la ley es, de una parte, lo interior, lo que es en sí y..."""
    },
    {
        "id": "e14",
        "pagina": 96,
        "texto": """porque, de otra parte, es en ella, al mismo tiempo, lo diferente. El que esta diferencia sea una diferencia interna viene dado en el hecho de que la ley es fuerza simple o como concepto de la diferencia, de que es, por tanto, una diferencia del concepto. Pero esta diferencia interna, al principio, corresponde solamente al entendimiento; no aparece todavía puesta en la cosa misma. El entendimiento expresa, pues, solamente la propia necesidad; una diferencia que sólo puede establecer en tanto que expresa al mismo tiempo que la diferencia no es una diferencia de la cosa misma. Esta necesidad, que sólo radica en las palabras, es, de este modo, la descripción de los momentos que forman el ciclo de dicha necesidad; se los distingue, evidentemente, pero al mismo tiempo, superada; este movimiento se llama explicación. Así, pues, se enuncia una ley, de la que se distingue como la fuerza su en sí universal o el fundamento; pero de esta diferencia se dice que no es tal, sino que el fundamento se halla más bien constituido como la ley. Por ejemplo, el suceso singular del rayo es aprehendido como universal y este universal se enuncia como la ley de la electricidad; la explicación resume luego la ley en la fuerza, como la esencia de la ley. Esta fuerza se halla, ahora, constituida de tal modo que, al exteriorizarse, brotan electricidades de signo opuesto, las cuales desaparecen de nuevo la una en la otra; es decir, que la fuerza se halla constituida exactamente lo mismo que la ley; se dice que no existe entre ambas diferencias alguna. Las diferencias son la pura exteriorización universal o la ley y la pura fuerza; pero ambas tienen el mismo contenido, la misma constitución; se revoca, por tanto, la diferencia como diferencia del contenido, es decir, como diferencia de la cosa.

En este movimiento tautológico, el entendimiento permanece, como se ve, en la unidad quieta de su objeto y el movimiento recae solamente en el entendimiento, y no en el objeto; es una explicación que no sólo no explica nada, sino que es tan clara, que, tratando de decir algo distinto de lo ya dicho, no dice en rigor nada y se limita a repetir lo mismo. En la cosa misma no nace con este movimiento nada nuevo, sino que el movimiento [sólo] se toma en consideración como movimiento del entendimiento. Sin embargo, en él reconocemos cabalmente aquello cuya ausencia se echaba de menos en la ley, a saber: el cambio absoluto mismo, pues este movimiento, si lo consideramos más de cerca, es de un modo inmediato lo contrario de sí mismo. Pone, en efecto, una diferencia que no sólo no es para nosotros ninguna diferencia, sino que él mismo supera como diferencia. Es el mismo cambio que se presentaba como el juego de fuerzas; en éste se daba la diferencia entre lo solicitante y lo solicitado, entre la fuerza exteriorizada y la fuerza repelida hacia sí misma, pero se trataba de diferencias que en realidad no eran tales y que, por tanto, volvían a superarse de un modo inmediato. Lo que se halla presente no es solamente la mera unidad, como si no se pusiera en ella diferencia alguna, sino este movimiento, que establece ciertamente una diferencia, pero una diferencia que, por no serlo, es nuevamente superada. Así, pues, con la explicación los cambios y mutaciones, que antes sólo se daban fuera de lo interior, en el fenómeno, han penetrado en lo suprasensible mismo; pero nuestra conciencia ha pasado de lo interior como objeto al otro lado, al entendimiento y encuentra aquí el cambio."""
    },
    {
        "id": "e15",
        "pagina": 97,
        "texto": """[γ] La ley de la pura diferencia, el mundo invertido]

Este cambio no es aún un cambio de la cosa misma, sino que se presenta más bien precisamente como cambio puro porque el contenido de los momentos del cambio sigue siendo el mismo. Pero, en cuanto el concepto como concepto del entendimiento es lo mismo que lo interior de las cosas, este cambio pasa a ser, para el entendimiento, la ley de lo interior. El entendimiento experimenta, pues, que es ley del fenómeno mismo el que lleguen a ser diferencias que no son tales o el que cosas homónimas se repelan de sí mismas; lo mismo que el que las diferencias son solamente aquellas que no lo son en verdad y que se superan o que las cosas no homónimas se atraigan. Una segunda ley, cuyo contenido se contrapone a lo que antes llamábamos ley, es decir, a la diferencia que permanecía constantemente igual a sí misma; pues esta nueva ley expresa más bien el convertirse lo igual en desigual y el convertirse lo desigual en igual. El concepto induce a la ausencia de pensamiento a reunir ambas leyes y a cobrar conciencia de su contraposición. Claro está que también la segunda se pone como ley o como un ser interior igual a sí mismo, pero una igualdad consigo mismo más bien de la desigualdad, una constancia de lo inconstante. En el juego de fuerzas, esta ley resultaba precisamente como este tránsito absoluto y como puro cambio; el homónimo, la fuerza, se descompone en una contraposición que primeramente se manifiesta como una diferencia independiente, pero que de hecho no demuestra ser tal diferencia; pues es lo homónimo lo que de sí mismo se repele, y lo repelido se atrae, por tanto, esencialmente, porque es lo mismo; por consiguiente, la diferencia establecida vuelve a superarse, puesto que no es tal diferencia. Esta se presenta, así, como diferencia de la cosa misma o como diferencia absoluta, y esta diferencia de la cosa no es, pues, sino lo homónimo que se ha repelido de sí mismo y pone, de este modo, una contraposición que no lo es.

Por medio de este principio, el primer suprasensible, el reino quieto de las leyes, la imagen inmediata del mundo percibido, se torna en su contrario; la ley era, en general, lo que permanecía igual, como sus diferencias; pero ahora se establece que ambas cosas, la ley y sus diferencias, son más bien lo contrario de sí mismas; lo igual a sí se repele más bien de sí mismo y lo desigual a sí se pone más bien como lo igual a sí. Sólo con esta determinación tenemos, de hecho, que la diferencia es la diferencia interna o la diferencia en sí misma, en cuanto lo igual es desigual a sí y lo desigual igual a sí. Este segundo mundo suprasensible es, de este modo, el mundo invertido; y ciertamente, en cuanto que un lado está presente ya en el primer mundo suprasensible, el mundo invertido de este primer mundo. Por donde lo interior se consuma como fenómeno. En efecto, el primer mundo suprasensible no era sino la elevación inmediata del mundo percibido al elemento universal; tenía su contraimagen necesaria en este mundo, que aún retenía para sí el principio del cambio y de la mutación; el primer reino de las leyes carecía de esto, pero lo adquiere ahora como mundo invertido.

Según la ley de este mundo invertido, lo homónimo del primero es, por tanto, lo desigual de sí mismo y lo desigual de dicho mundo es asimismo desigual a sí mismo o deviene igual a sí. En determinados momentos resultará que lo que en la ley del primero era dulce es en la de este invertido en sí amargo, y lo que en aquélla ley era negro es en éste blanco. Lo que en la ley del primero era el polo Norte de la brújula es en su otro en sí suprasensible (es decir, en la tierra) el polo Sur, y lo que allí es polo Sur es aquí polo Norte. Del mismo modo, lo que en la primera ley de la electricidad es el polo del oxígeno se convierte, en su otra esencia suprasensible, en el polo del hidrógeno; y, viceversa, lo que allí es el polo del hidrógeno se convierte aquí en el polo del oxígeno. En otra esfera, vemos que, con arreglo a la ley inmediata, el vengarse del enemigo constituye la más alta satisfacción de la individualidad atropellada. Pero esta ley, según la cual debo mostrarme como esencia contra quien se niega a tratarme como esencia independiente, y suprimirlo a él más bien como esencia, se invierte por el principio del otro mundo en lo opuesto, y la restauración de mí mismo como esencia mediante la superación en la esencia del otro se convierte en autodestrucción. Ahora bien, si esta inversión que se representa en el castigo del delito se convierte en ley, tampoco ésta es sino la ley de un mundo que tiene que enfrentarse a un mundo suprasensible invertido, en el que se honra lo que en aquél se desprecia y se desprecia lo que en aquél se honra. La pena, que según la ley del primero infama y aniquila al hombre, se trueca en su mundo invertido en el perdón que mantiene a salvo su esencia y lo honra."""
    },
    {
        "id": "e16",
        "pagina": 98,
        "texto": """Visto superficialmente, este mundo invertido es lo contrario del primero, de tal manera que lo tiene fuera de él y lo repele de sí como una realidad invertida; de modo que uno es el fenómeno y el otro, en cambio, el en sí, el uno el mundo como es para otro, el otro, por el contrario, como es para sí; por donde, para seguir empleando los anteriores ejemplos, lo que sabe dulce es, propiamente o en el interior de la cosa, amargo, o lo que en la brújula real del fenómeno es el polo Norte es en el ser interior o esencial el polo Sur; y lo que en la electricidad fenoménica se manifiesta como el polo del oxígeno sería en la no fenoménica el polo del hidrógeno. O bien un acto que como fenómeno es un delito debería en su interior poder ser propiamente bueno (un acto malo animado por una intención buena) y la pena ser un castigo solamente como manifestación, pero en sí o en otro mundo constituir un beneficio para el delincuente. Sin embargo, aquí ya no se dan esos antagonismos entre lo interno y lo externo, el fenómeno y lo suprasensible, como dos tipos de realidades. Las diferencias repelidas ya no se reparten de nuevo entre dos sustancias de éstas que sean portadoras de ellas y les confieran una subsistencia separada, de tal modo que el entendimiento, brotando de lo interior, se reintegrara a su puesto anterior. Uno de los lados o una de las sustancias volvería a ser el mundo de la percepción, en el que ejercería su esencia una de las dos leyes, y frente a él aparecería un mundo interior, que sería exactamente un mundo sensible como el primero, pero en la representación; no podría ser mostrado, visto, oído ni gustado como mundo sensible, pero sería representado como un mundo sensible semejante. Pero, de hecho, si uno de los elementos puestos es algo percibido y su en sí, como lo invertido de ello es asimismo algo representado de un modo sensible, tenemos que lo amargo, que sería el en sí de la cosa dulce, es una cosa tan real como ella una cosa amarga; lo negro, que sería el en sí de lo blanco es lo negro real; el polo Norte, que es el en sí del polo Sur, es el polo Norte presente en la misma brújula; el polo de oxígeno que es el en sí del polo de hidrógeno, es el polo de oxígeno presente en la misma columna. Y el delito real tiene su inversión y su en sí, como posibilidad, en la intención como tal, pero no es una buena intención, pues la verdad de la intención es sólo el hecho mismo. Y, según su contenido, el delito tiene su reflexión en sí mismo o su inversión en la pena real; ésta es la reconciliación de la ley con la realidad."""
    },
    {
        "id": "e17",
        "pagina": 99,
        "texto": """que se le opone en el delito. Por último, la pena real tiene su realidad invertida en ella misma, que es una realización de la ley, de tal modo que la que tiene ésta como pena se supera a sí misma, se convierte de nuevo de ley activa en ley quieta y vigente, cancelándose el movimiento de la individualidad en contra de la ley y el de ella en contra de la individualidad.

### [3. La infinitud]

Así, pues, de la representación de la inversión, que constituye la esencia de uno de los lados del mundo suprasensible hay que alejar la representación sensible del afianzamiento de las diferencias en un elemento distinto de la subsistencia y representarse y concebir en su pureza este concepto absoluto de la diferencia como diferencia interna, como el repeler de sí mismo lo homónimo como homónimo y el ser igual de lo desigual como desigual. Hay que pensar el cambio puro o la contraposición en sí misma, la contradicción. En efecto, en la diferencia que es una diferencia interna lo opuesto no es solamente uno de dos —pues, de otro modo, sería un algo que es, y no un opuesto—, sino que es lo opuesto de algo opuesto; lo otro es dado inmediatamente en él mismo. Indudablemente, coloco lo contrario del lado de acá y del lado de allá lo otro, con respecto a lo cual es lo contrario; por tanto, pongo lo contrario de un lado, en y para sí sin lo otro. Pero, cabalmente al tener aquí lo opuesto en y para sí, es lo contrario de sí mismo o tiene ya de hecho inmediatamente lo otro en él mismo. Y así, el mundo suprasensible, que es el mundo invertido, ha sobrepasado al mismo tiempo al otro y lo ha incluido en sí mismo; es para sí el mundo invertido, es decir, la inversión de sí mismo; es él mismo y su contraposición en una unidad. Solamente así es la diferencia como diferencia interna o diferencia en sí misma, o como infinitud.

A través de la infinitud vemos que la ley se ha realizado plenamente en ella misma como necesidad y que todos los momentos del fenómeno han sido recogidos ahora en su interior. El que lo simple de la ley es la infinitud significa, como resultado de lo que antecede: a) que la ley es algo igual a sí mismo, que es, sin embargo, la diferencia en sí, o que es un homónimo que se repele de sí mismo o se desdobla. Lo que se llamaba fuerza simple se duplica a sí misma y es por su infinitud la ley. b) Lo desdoblado, que constituye las partes representadas en la ley, se presenta como subsistente; estas partes, consideradas sin el concepto de la diferencia interna, son el espacio y el tiempo o la distancia y la velocidad que brotan como momentos..."""
    },
    {
        "id": "e18",
        "pagina": 100,
        "texto": """de la gravedad, indiferentes y no necesarios tanto el uno con respecto al otro como en relación con la misma gravedad, lo mismo que esta gravedad simple con respecto a ellos o la electricidad simple con respecto a la electricidad positiva y negativa [indiferente]. Y ahora bien, a través del concepto de la diferencia interna este algo desigual e indiferente, espacio y tiempo, etc., es una diferencia que no es tal diferencia o sólo es diferencia de lo homónimo y su esencia es la unidad; esos elementos son animados el uno con respecto al otro como lo positivo y lo negativo, y su ser es más bien el ponerse como no ser y superarse en la unidad. Ambos términos diferentes subsisten y son en sí, son en sí como contrapuestos, es decir, son cada uno de ellos lo contrapuesto a sí mismo, tienen su otro en ellos y son solamente una unidad.

Esta infinitud simple o el concepto absoluto debe llamarse la esencia simple de la vida, el alma del mundo, la sangre universal, omnipresente, que no se ve empañada ni interrumpida por ninguna diferencia, sino que más bien es ella misma todas las diferencias así como su ser superado y que, por tanto, palpita en sí sin moverse, tiembla en sí sin ser inquieta. Esta infinitud simple es igual a sí misma, pues las diferencias son tautológicas; son diferencias que no lo son. Por tanto, esta esencia igual a sí misma se relaciona consigo misma solamente; consigo misma, por donde esto es un otro al que la relación tiende, y la relación consigo misma es más bien el desdoblamiento, o bien aquella igualdad consigo misma es diferencia interna. Estos términos desdoblados son, por tanto, en y para sí mismos, cada uno de ellos un contrario de otro, por donde el otro se enuncia ya al mismo tiempo que él. Dicho en otros términos, cada término no es el contrario de un otro, sino solamente el contrario puro; de este modo, por tanto, es en él mismo lo contrario de sí. O bien no es en general un contrario, sino que es puramente para sí, una esencia pura igual a sí misma, que no tiene en ella diferencia alguna; de este modo, no necesitamos presentar, y menos aún considerar como filosofía el atormentarnos con esta indagación, o incluso considerar como insoluble el problema de saber cómo brota la diferencia o el ser otro partiendo de esta esencia pura y fuera de ella; pues el desdoblamiento se ha producido ya y la diferencia ha quedado excluida de lo igual a sí mismo y ha sido dejada a un lado; por tanto, lo que debiera ser lo igual a sí mismo se ha convertido ya en uno de los términos del desdoblamiento, en lugar de ser la esencia absoluta. Decir que lo igual a sí mismo se desdobla equivale, pues, a decir, exactamente lo mismo, que se supera como ya desdoblado, que se supera como ser otro. La unidad, de la que suele decirse que..."""
    },
    {
        "id": "e19",
        "pagina": 101,
        "texto": """de ella no puede brotar la diferencia, no es de hecho, ella misma, solamente momento del desdoblamiento; es la abstracción de la simplicidad enfrentada a la diferencia. Pero, al ser la abstracción, solamente uno de los elementos contrapuestos, queda dicho con ello que es el desdoblamiento, pues si la unidad es algo negativo, algo contrapuesto, cabalmente es puesto así como lo que tiene en él la contraposición. Por tanto, las diferencias entre el desdoblamiento y el devenir igual a sí mismo son también, por consiguiente, tan sólo este movimiento del superarse; pues en cuanto lo igual a sí mismo que debe desdoblarse o convertirse en su contrario es una abstracción o el mismo algo ya desdoblado, tenemos que su desdoblamiento es, con ello, una superación de lo que es y, por ende, la superación de su ser desdoblado. El devenir igual a sí mismo es igualmente un desdoblarse; lo que deviene igual a sí mismo se enfrenta, así, al desdoblamiento; es decir, se pone a sí mismo de lado o deviene más bien algo desdoblado.

La infinitud o esta inquietud absoluta del puro moverse a sí mismo, según lo cual lo determinado de algún modo, por ejemplo, como ser, es más bien lo contrario de esta determinabilidad, es, ciertamente, el alma de todo el recorrido anterior, pero solamente en el interior ha surgido ella misma libremente. La manifestación o el juego de fuerzas la presenta ya a ella misma, pero sólo surge libremente por vez primera como explicación; y como, por último, es objeto para la conciencia como lo que ella es, la conciencia es autoconciencia. La explicación del entendimiento sólo es, de momento, la descripción de lo que la autoconciencia es. El entendimiento supera las diferencias presentes en la ley, ya convertidas en diferencias puras, pero todavía indiferentes, y las pone en una unidad, que es la fuerza. Pero este devenir igual es también, no menos inmediatamente, un desdoblamiento, pues sólo supera las diferencias y pone lo uno de la fuerza al establecer una nueva diferencia, la de ley y fuerza, que, empero, al mismo tiempo no es tal diferencia; y precisamente porque esta diferencia, al mismo tiempo, no lo es, el entendimiento procede él mismo una vez más a la superación de esta diferencia; haciendo que la fuerza se halle constituida del mismo modo que la ley. Pero, así, este movimiento o esta necesidad siguen siendo todavía necesidad y movimiento del entendimiento o no son, en cuanto tales, su objeto, sino que el entendimiento tiene como objetos, la electricidad positiva y negativa, la distancia, la velocidad, la fuerza de atracción y mil cosas más, que forman el contenido de los momentos del movimiento. En la explicación encontramos cabalmente mucha autosatisfacción, porque aquí la conciencia, para decirlo así, se halla en coloquio..."""
    },
    {
        "id": "e20",
        "pagina": 102,
        "texto": """inmediato consigo misma, gozándose solamente a sí misma; parece ocuparse de otra cosa, pero de hecho sólo se ocupa de sí misma.

En la ley opuesta, como la inversión de la primera ley, o en la diferencia interna, es cierto que la infinitud misma deviene objeto del entendimiento, pero éste la pierde de nuevo en cuanto tal, al repartir de nuevo en dos mundos o en dos elementos sustanciales la diferencia en sí, el repelerse a sí mismo de lo homónimo y los términos desiguales que se atraen; el movimiento tal y como es en la experiencia es aquí, para él, un acaecer y lo homónimo y lo desigual son predicados cuya esencia es un substrato que es. Lo mismo que para el entendimiento es un objeto bajo envoltura sensible, es para nosotros, en su figura esencial como concepto puro. Esta aprehensión de la diferencia como en verdad es o la aprehensión de la infinitud como tal es para nosotros o en sí. La exposición de su concepto corresponde a la ciencia; pero la conciencia, en cuanto lo posee de un modo inmediato, reaparece como forma propia o nueva figura de la conciencia, que en lo que precede no conoce su esencia, sino que ve en ella algo completamente distinto. Al convertirse en su objeto este concepto de la infinitud, ella es, por tanto, conciencia de la diferencia, como diferencia también inmediatamente superada; la conciencia es para sí misma, es la diferenciación de lo indistinto o autoconciencia. Yo me distingo de mí mismo, y en ello es inmediatamente para mí el que este distinto no es distinto. Yo, lo homónimo, me repele de mí mismo; pero este algo diferenciado, puesto como algo desigual, no es de modo inmediato, en cuanto diferenciado, ninguna diferencia para mí. La conciencia de un otro, de un objeto en general, es, ciertamente, ella misma, necesariamente autoconciencia, ser reflejado en sí, conciencia de sí misma en su ser otro. El proceso necesario de las figuras anteriores de la conciencia, para la que lo verdadero era una cosa, un otro que ella misma, expresa cabalmente que no sólo la conciencia de la cosa sólo es posible para una conciencia de sí, sino, además, que solamente ésta es la verdad de aquellas figuras. Pero esta verdad sólo se da para nosotros, aún no para la conciencia. La conciencia de sí sólo ha devenido para sí, pero aún no como unidad con la conciencia en general.

Vemos que en el interior de la manifestación el entendimiento no es en verdad otra cosa que la manifestación misma, pero no tal y como es en cuanto juego de fuerzas, sino más bien este mismo juego de fuerzas en sus momentos absolutamente universales y en el movimiento de éstos, y de hecho, el entendimiento sólo se experimenta a sí mismo. Elevada por sobre la percepción, la conciencia se presenta unida a lo suprasensible por medio de la manifestación,..."""
    },
    {
        "id": "e21",
        "pagina": 104,
        "texto": """104 CONCIENCIA

a través de la cual mira a este fondo. Los dos extremos, uno el del puro interior y otro el del interior que mira a este interior puro, se juntan ahora y, lo mismo que desaparecen ellos como extremos, desaparece también el término medio, en cuanto algo distinto que ellos. Se alza, pues, este telón sobre lo interior y lo presente es el acto por el que lo interior mira lo interior; la contemplación del homónimo no diferenciado que se repele a sí mismo se pone como lo interior diferente, pero para lo cual es igualmente inmediata la no diferenciabilidad de ambos términos, la autoconciencia. Y se ve que detrás del llamado telón, que debe cubrir el interior, no hay nada que ver, a menos que penetremos nosotros mismos tras él, tanto para ver, como para que haya detrás algo que pueda ser visto. Pero se muestra, al mismo tiempo, que no era posible pasar directamente hacia allí, sin preocuparse de todas estas circunstancias, ya que este saber que es la verdad de la representación del fenómeno y de su interior sólo es, a su vez, el resultado de un movimiento circunstanciado, a lo largo del cual desaparecen los modos de la conciencia, el modo de ver, la percepción y el entendimiento; y se mostrará, al mismo tiempo, que el conocimiento de lo que la conciencia sabe, en cuanto se sabe a sí misma, exige todavía mayores circunstancias, que pasamos a examinar a continuación."""
    }
]

# Notas de análisis del Capítulo III
NOTAS_ENTENDIMIENTO = {
    "e01": "Fragmento e01 (p82): Introducción al entendimiento; el universal incondicionado como nuevo objeto; distinción entre concepto en sí y para la conciencia.",
    "e02": "Fragmento e02 (p83): Desarrollo del universal incondicionado; la fuerza como unidad de ser para sí y ser para otro; anuncio del juego de fuerzas.",
    "e03": "Fragmento e03 (p85): Concepto de fuerza, su realización, desdoblamiento en dos fuerzas.",
    "e04": "Fragmento e04 (p86): Juego de fuerzas, solicitación mutua, trueque de determinabilidades, independencia ilusoria.",
    "e05": "Fragmento e05 (p87): Doble diferencia (contenido/forma) en el juego de fuerzas; disolución de la independencia; la fuerza como puro concepto.",
    "e06": "Fragmento e06 (p88): Lo interior; el mundo suprasensible como esencia; la fuerza deviene concepto.",
    "e07": "Fragmento e07 (p89): El fenómeno como manifestación; el mundo suprasensible como verdad del fenómeno.",
    "e08": "Fragmento e08 (p90): Crítica al incognoscible; el mundo suprasensible es vacío y se llena con sueños; pero es el fenómeno como fenómeno.",
    "e09": "Fragmento e09 (p91): La ley como verdad de la manifestación; el juego de fuerzas se reduce a diferencia universal; la ley como imagen constante.",
    "e10": "Fragmento e10 (p92): El reino de las leyes; la diferencia universal; la ley es la imagen constante del fenómeno; anuncio de que la ley no agota la manifestación.",
    "e11": "Fragmento e11 (p93): Crítica de la multiplicidad de leyes; la atracción universal como concepto vacío de ley.",
    "e12": "Fragmento e12 (p94): Relación entre fuerza y ley; ejemplos de electricidad y gravedad; indiferencia del concepto; la necesidad es vacía.",
    "e13": "Fragmento e13 (p95): Indiferencia de ley y fuerza; necesidad vacía; crítica de la explicación.",
    "e14": "Fragmento e14 (p96): La explicación tautológica; el cambio absoluto penetra en lo interior.",
    "e15": "Fragmento e15 (p97): El mundo invertido; ejemplos de inversión; la ley de la pura diferencia.",
    "e16": "Fragmento e16 (p98): Crítica de la dualidad de mundos; la infinitud como unidad; tránsito a la autoconciencia.",
    "e17": "Fragmento e17 (p99): La infinitud como culminación del entendimiento; la diferencia interna.",
    "e18": "Fragmento e18 (p100): La infinitud como esencia simple, alma del mundo; la unidad de los opuestos.",
    "e19": "Fragmento e19 (p101): La infinitud como movimiento; la conciencia deviene autoconciencia.",
    "e20": "Fragmento e20 (p102): La explicación como autosatisfacción; la infinitud como objeto; la autoconciencia emerge.",
    "e21": "Fragmento e21 (p104): Conclusión: el telón se levanta; la autoconciencia es la verdad del entendimiento."
}

# Ejemplos concretos del Capítulo III
EJEMPLOS_ENTENDIMIENTO = {
    "e03": [{"tipo": "fuerza", "descripcion": "Fuerza que se exterioriza y retorna a sí", "ejemplo": "análogo a la fuerza magnética"}],
    "e04": [{"tipo": "juego de fuerzas", "descripcion": "Dos fuerzas que se solicitan mutuamente, trueque de roles", "ejemplo": "acción y reacción"}],
    "e07": [{"tipo": "mundo suprasensible", "descripcion": "El más allá del fenómeno, verdad del mundo sensible", "ejemplo": "reino de leyes"}],
    "e10": [{"tipo": "ley", "descripcion": "Imagen constante del fenómeno", "ejemplo": "ley de la atracción universal"}],
    "e12": [
        {"tipo": "electricidad", "descripcion": "Fuerza simple que se manifiesta como positiva y negativa", "ley": "ley de la electricidad"},
        {"tipo": "gravedad", "descripcion": "Fuerza simple cuya ley relaciona tiempo y espacio (raíz y cuadrado)", "ley": "ley de caída"}
    ],
    "e15": [
        {"tipo": "brújula", "descripcion": "El polo Norte en el fenómeno es polo Sur en el mundo invertido", "ley": "inversión"},
        {"tipo": "electricidad", "descripcion": "El polo del oxígeno en el fenómeno es polo del hidrógeno en el mundo invertido", "ley": "inversión"},
        {"tipo": "venganza", "descripcion": "La venganza (afirmación del yo) se invierte en autodestrucción", "ley": "inversión ética"},
        {"tipo": "castigo", "descripcion": "El castigo (infamia) se invierte en perdón (gracia)", "ley": "inversión ética"}
    ]
}

# Momentos dialécticos del Capítulo III
MOMENTOS_ENTENDIMIENTO = [
    "transición desde la percepción",
    "universal incondicionado como nuevo objeto",
    "distinción concepto en sí / para la conciencia",
    "el entendimiento como contemplación pasiva",
    "la fuerza como unidad de ser para sí y ser para otro",
    "exteriorización de la fuerza",
    "juego de fuerzas y solicitación mutua",
    "desdoblamiento en dos fuerzas",
    "trueque de determinabilidades (solicitante/solicitada)",
    "la independencia ilusoria de las fuerzas",
    "el juego como unidad del movimiento",
    "doble diferencia (contenido/forma)",
    "disolución de la independencia",
    "la fuerza como puro concepto",
    "postulación del mundo suprasensible",
    "lo interior como esencia verdadera",
    "el fenómeno como manifestación",
    "el mundo suprasensible como verdad del fenómeno",
    "crítica al incognoscible",
    "el mundo suprasensible es vacío",
    "el mundo suprasensible se llena con sueños",
    "el mundo suprasensible es el fenómeno en cuanto fenómeno",
    "la ley como verdad de la manifestación",
    "la ley como imagen constante",
    "el reino de las leyes",
    "la diferencia universal",
    "la ley no agota la manifestación",
    "crítica de la multiplicidad de leyes",
    "unificación en la atracción universal (vacía)",
    "distinción entre ley universal y leyes determinadas",
    "relación entre fuerza y ley",
    "ejemplo: electricidad (positiva/negativa)",
    "ejemplo: gravedad (caída)",
    "indiferencia del concepto respecto al ser",
    "la necesidad como palabra vacía",
    "explicación tautológica",
    "cambio absoluto en lo interior",
    "postulación del mundo invertido",
    "inversión: polo Norte/Sur",
    "inversión: oxígeno/hidrógeno",
    "inversión: venganza/autodestrucción",
    "inversión: castigo/perdón",
    "crítica de la dualidad de mundos",
    "unificación en la infinitud",
    "la infinitud como diferencia interna",
    "la ley se realiza en la infinitud",
    "la infinitud como esencia simple, alma del mundo",
    "la conciencia se encuentra a sí misma en la explicación",
    "la autoconciencia emerge como verdad del entendimiento",
    "tránsito a la autoconciencia"
]

# Metáforas clave del Capítulo III
METAFORAS_ENTENDIMIENTO = [
    "universal incondicionado", "fuerza", "juego de fuerzas", "exteriorización", "solicitación",
    "ley", "fenómeno", "mundo suprasensible", "concepto", "reflexión", "ser para sí", "ser para otro",
    "forma", "contenido", "tautología", "entendimiento", "esencia", "manifestación", "apariencia",
    "fuerza repelida", "dualidad", "trueque de determinabilidades", "desaparición", "retorno a sí",
    "fuerza solicitante", "fuerza solicitada", "interior", "reino de las leyes", "diferencia universal",
    "imagen constante", "atracción universal", "electricidad", "positiva", "negativa", "gravedad",
    "caída", "tiempo", "espacio", "distancia", "velocidad", "raíz", "cuadrado", "propiedad",
    "definición", "indiferencia", "mundo invertido", "polo Norte", "polo Sur", "brújula",
    "oxígeno", "hidrógeno", "venganza", "castigo", "perdón", "infinitud", "auto-negación",
    "auto-relación", "contradicción", "diferencia interna", "auto-repulsión", "auto-inversión",
    "unidad de opuestos", "alma del mundo", "sangre universal", "telón", "autoconciencia"
]

# -------------------------------------------------------------------
# DATOS DEL CAPÍTULO IV (FRAGMENTOS COMPLETOS)
# -------------------------------------------------------------------

FRAGMENTOS_CAPITULO4 = [
    {
        "id": "ac01",
        "pagina": 107,
        "texto": """IV. LA VERDAD DE LA CERTEZA DE SI MISMO

En los modos de la certeza que preceden lo verdadero es para la conciencia algo distinto a ella misma. Pero el concepto de este algo verdadero desaparece en la experiencia de él; el objeto no se muestra ser en verdad como era de un modo inmediato en sí, como lo que es de la certeza sensible, la cosa concreta de la percepción, la fuerza del entendimiento, sino que este en sí resulta ser un modo en que es solamente para otro; el concepto del objeto se supera en el objeto real o la primera representación inmediata en la experiencia, y la certeza se pierde en la verdad. Pero, ahora ha nacido lo que no se producía en estos comportamientos anteriores: una certeza que es igual a su verdad, pues la certeza es ella misma su objeto y la conciencia es ella misma lo verdadero. Y en ello es también, ciertamente, un ser otro; en efecto, la conciencia distingue, pero distingue algo que para ella es, al mismo tiempo, algo no diferenciado. Si llamamos concepto al movimiento del saber y objeto al saber, pero como unidad quieta o como yo, vemos que, no solamente para nosotros, sino para el saber mismo, el objeto corresponde al concepto. O bien, si, de otro modo, llamamos concepto a lo que el objeto es en sí y objeto a lo que es como objeto o para otro, vemos que es lo mismo el ser en sí y el ser para otro, pues el en sí es la conciencia; pero es también aquello para lo que es otro (el en sí); y es para ella para lo que el en sí del objeto y el ser del mismo para otro son lo mismo; el yo es el contenido de la relación y la relación misma; es el mismo contra otro y sobrepasa al mismo tiempo este otro, que para él es también sólo el mismo."""
    },
    {
        "id": "ac02",
        "pagina": 107,
        "texto": """[1. La autoconciencia en sí]

Con la autoconciencia entramos, pues, en el reino propio de la verdad. Hay que ver cómo comienza surgiendo esta figura de la autoconciencia. Si consideramos esta nueva figura del saber, el saber de sí mismo, en relación con la anterior, con el saber de otro, vemos que este último ha desaparecido, ciertamente, pero sus momentos, al mismo tiempo, se han conservado, y la pérdida consiste en que dichos momentos están presentes aquí tal y como son en sí. El ser de la suposición, lo singular y, contrapuesta a ella, la universalidad de la percepción, al igual que el interior vacío del entendimiento no son ya como esencias, sino como momentos de la autoconciencia, es decir, como abstracciones o diferencias que para la conciencia son ellas mismas, al mismo tiempo, nulas o no son tales diferencias, sino esencias que tienden puramente a desaparecer. Así, pues, sólo parece haberse perdido el momento principal mismo, a saber: la subsistencia simple independiente para la conciencia. Pero, de hecho, la autoconciencia es la reflexión, que desde el ser del mundo sensible y percibido, es esencialmente el retorno desde el ser otro. Como autoconciencia, es movimiento; pero, en cuanto se distingue solamente si mismo como el sí mismo de sí, la diferencia es superada para ella de un modo inmediato como un ser otro; la diferencia no es, y la autoconciencia es solamente la tautología sin movimiento del yo soy yo; en cuanto que para ella la diferencia no tiene tampoco la figura del ser, no es autoconciencia. Así, pues, para ella el ser otro es como un ser o como un momento diferenciado; pero para ella es también la unidad de sí misma con esta diferencia como segundo momento diferenciado. Con aquel primer momento la autoconciencia es como conciencia y para ella se mantiene toda la extensión del mundo sensible, pero, al mismo tiempo, sólo como referida al segundo momento, a la unidad de la autoconciencia consigo misma; por consiguiente, el mundo sensible es para ella una subsistencia, pero una subsistencia que es solamente manifestación o diferencia, que no tiene en sí ser alguno. Pero esta contraposición entre su fenómeno y su verdad sólo tiene por su esencia la verdad, o sea la unidad de la conciencia consigo misma; esta unidad debe ser esencial a la autoconciencia; es decir, que ésta es, en general, apetencia. La conciencia tiene ahora, como autoconciencia, un doble objeto: uno, el objeto inmediato de la certeza sensible y de la percepción, pero que se halla señalado para ella con el carácter de lo negativo, y el segundo, precisamente ella misma, que es la verdadera esencia y que de momento sólo está presente en la contraposición del primero. La autoconciencia se presenta aquí como el movimiento en que esta contraposición se ha superado y en que deviene la igualdad de sí misma consigo misma."""
    },
    {
        "id": "ac03",
        "pagina": 108,
        "texto": """[2. La vida]

El objeto, que para la autoconciencia es lo negativo, es a la vez, para nosotros o en sí, algo retomado a sí mismo, como por su parte la conciencia. A través de esta reflexión, en sí mismo, el objeto ha devenido vida. Lo que la autoconciencia distingue de sí misma como lo que es tiene también en sí, en cuanto se lo pone como lo que es, no sólo el modo de la certeza sensible y de la percepción, sino que es ser reflejado en sí mismo, y el objeto de la apetencia inmediata es algo vivo. En efecto, el en si o el resultado universal del comportamiento del entendimiento hacia el interior de las cosas es la diferenciación de lo diferenciable o la unidad de lo diferenciado. Pero esta unidad es, asimismo, como hemos visto, el repelerse de sí misma; y este concepto se escribe en la contraposición entre la autoconciencia y la vida, aquélla es la unidad para la que es la unidad infinita de las diferencias; pero ésta es solamente esta unidad misma, de tal modo que no es al mismo tiempo para sí misma. Tan independiente, por tanto, como la conciencia lo es en sí su objeto. La auto-conciencia, que es simplemente para sí y que marca de un modo inmediato su objeto con el carácter de lo negativo o es ante todo apetencia, será más bien la que pase por la experiencia de la independencia de dicho objeto.

La determinación de la vida, tal como se deriva del concepto o del resultado universal con que hemos entrado en esta esfera hasta para caracterizar la vida, sin necesidad de seguir desarrollando su naturaleza; su ciclo se cierra con los siguientes momentos: 'La esencia es la infinitud como el ser superado de todas las diferencias, el puro movimiento de rotación alrededor de su eje, la quietud de sí misma como infinitud absolutamente inquieta; la independencia misma, en la que se disuelven las diferencias del movimiento; la esencia simple del tiempo, que tiene en esta igualdad consigo misma la figura compacta del espacio. Pero, en este médium simple y universal, las diferencias son también como diferencias, pues esta fluidez universal sólo tiene su naturaleza negativa en cuanto es una superación de ellas; pero no puede superar las diferencias si éstas no tienen subsistencia.' Y es precisamente dicha fluidez la que, como independencia igual a sí misma, es ella misma la subsistencia o la sustancia de ellas, en la cual ellas son, por tanto, como miembros diferenciados y partes que son para sí. El ser no tiene ya el significado de la abstracción del ser, ni la esencialidad pura de dichos miembros (la de la) abstracción de la universalidad, sino que su ser es cabalmente aquella simple sustancia fluida del puro movimiento en sí mismo. Pero la diferencia de estos miembros entre sí como diferencia, no consiste en general en ninguna otra determinabilidad que la determinabilidad de los momentos de la infinitud o del puro movimiento mismo.

Los miembros independientes son para sí; pero este ser para sí es más bien del mismo modo inmediato su reflexión en la unidad, en cuanto esta unidad es, a su vez, el desdoblamiento en las figuras independientes. La unidad se ha desdoblado, porque es una unidad absolutamente negativa o infinita; y por ser la subsistencia, tenemos que la diferencia sólo tiene también independencia en ella. Esta independencia de la figura aparece como algo determinado, como algo para otro, pues es algo desdoblado; y, en este sentido, la superación de la escisión se lleva a cabo por medio de un otro. Pero, dicha superación se da también en ella misma, ya que cabalmente aquella fluidez es la sustancia de las figuras independientes; pero esta sustancia es infinita; por consiguiente, en su subsistencia misma es la figura el desdoblamiento o la superación de su ser para sí."""
    },
    {
        "id": "ac04",
        "pagina": 110,
        "texto": """Si distinguimos más de cerca los momentos que aquí se contienen, vemos que tenemos como primer momento la subsistencia de las figuras independientes o la represión de lo que es la diferenciación en sí, es decir, el no ser en sí y el carecer de subsistencia propia. El segundo momento es la sujección de aquella subsistencia bajo la infinitud de la diferencia. En el primer momento la figura subsistente es: como algo que es para sí o sustancia infinita en su determinabilidad, se aparece en contra de la sustancia universal, niega esta fluidez y continuidad con ella y se afirma como algo que no ha sido disuelto en este universal, sino que más bien se mantiene al disociarse de esta su naturaleza inorgánica y devorándola. En el médium fluido universal, que es un despliegue quieto de las figuras, la vida deviene precisamente por ello el movimiento de las mismas, se convierte en la vida como proceso. La fluidez simple y universal es el en sí y la diferencia entre las figuras lo otro. Pero esta fluidez deviene ella misma, por medio de esta diferencia, lo otro; pues ahora es para la diferencia, que es en y para sí misma y, por tanto, el movimiento infinito por el que es devorado aquel medio quieto, la vida como lo vivo. Pero esta inversión es, por ello, a su vez, la inversión en sí misma; lo devorado es la esencia; la individualidad, que se mantiene a costa de lo universal y que se asigna el sentimiento de su unidad consigo misma supera precisamente por ello su oposición con respecto a lo otro, por la que es para sí; la unidad consigo misma que se da es cabalmente la fluidez de las diferencias o la disolución universal. Pero, a la inversa, la superación de la subsistencia individual es también su producción. En efecto, como la esencia de la figura individual es la vida universal y lo que es para sí es en sí sustancia simple, al poner en sí lo otro supera esta simplicidad o su esencia, es decir, la desdobia, y este desdoblamiento de la fluidez indiferenciada es precisamente el poner la individualidad. Por tanto, la sustancia simple de la vida es el desdoblamiento de esta misma en figuras y, al mismo tiempo, la disolución de estas diferencias subsistentes; y la disolución del desdoblamiento es, asimismo, desdoblamiento o articulación de miembros. De este modo, los dos lados de todo el movimiento que han sido diferenciados, a saber: la plasmación de figuras quietamente desplegadas en el médium universal de la independencia, de una parte, y de otra el proceso de la vida caen el uno en el otro; el segundo es tanto configuración como superación de la figura; y el primero, la plasmación de figuras, es tanto superación como articulación de miembros. El elemento fluido es él mismo solamente la abstracción de la esencia; en otras palabras, sólo es real como figura; y al articularse en miembros desdobla, al mismo tiempo, lo articulado o lo disuelve. Todo este ciclo constituye la vida, que no es lo que primeramente se había dicho, la continuidad inmediata y la solidez de su esencia, ni la figura subsistente y lo discreto que es para sí, ni el puro proceso de ellos, ni tampoco la simple agrupación de estos momentos, sino el todo que se desarrolla, disuelve su desarrollo y se mantiene simplemente en este movimiento."""
    },
    {
        "id": "ac05",
        "pagina": 111,
        "texto": """[3. El yo y la apetencia]

En cuanto que, partiendo de la primera unidad inmediata y pasando por los momentos de la configuración y del proceso de retorno a la unidad de estos dos momentos y, con ello, a la primera sustancia simple, es que esta unidad reflejada es otra que la primera. Frente a aquella unidad inmediata o expresada como un ser, esta segunda es la unidad universal, que tiene en ella, como superados, todos estos momentos. Es el género simple, que en el movimiento de la vida misma no existe para sí como esto simple, sino que en este resultado la vida remite a un otro de lo que ella es precisamente, a la conciencia, para la que la vida es como esta unidad o como género.

Ahora bien, esta otra vida, para la que el género es como tal y que es para sí misma género, la autoconciencia sólo comienza siendo para sí como esta esencia simple y se tiene por objeto como yo puro; a lo largo de su experiencia, que ahora hay que pararse a considerar, este objeto abstracto se enriquecerá para ella y adquirirá el despliegue que hemos visto en la vida.

El simple yo sólo es este género o lo simple universal para lo que las diferencias no lo son en cuanto es la esencia negativa de los momentos independientes que se han configurado; por donde la autoconciencia sólo está cierta de sí misma mediante la superación de este otro, que aparece ante ella como vida independiente; es una apetencia. Cierta de la nulidad de este otro, pone para sí esta nulidad como su verdad, aniquila el objeto independiente y se da con ello la certeza de sí misma como verdadera certeza, como una certeza que ha devenido para ella misma de modo objetivo.

Pero, en esta satisfacción la autoconciencia pasa por la experiencia de la independencia de su objeto. La apetencia y la certeza de sí misma alcanzada en su satisfacción se hallan condicionadas por el objeto, ya que la satisfacción se ha obtenido mediante la superación de este otro; para que esta superación sea, tiene que ser este otro. Por tanto, la autoconciencia no puede superar al objeto mediante su actitud negativa ante él; lejos de ello, lo reproduce así, como reproduce la apetencia. Es, en realidad, un otro que la autoconciencia, la esencia de la apetencia; y gracias a esta experiencia ha devenido para ella misma esta verdad. Pero, al mismo tiempo, la autoconciencia es también absolutamente para sí, y lo es solamente mediante la superación del objeto y éste tiene que llegar a ser su satisfacción, puesto que es la verdad. Por razón de la independencia del objeto, la autoconciencia sólo puede, por tanto, lograr satisfacción en cuanto que este objeto mismo cumple en él la negación; y tiene que cumplir en sí esta negación de sí mismo, pues el objeto es en sí lo negativo y tiene que ser para otro lo que él es. En cuanto que el objeto es en sí mismo la negación y en la negación es al mismo tiempo independiente, es conciencia. En la vida, que es el objeto de la apetencia, la negación o bien es en un otro, a saber, en la apetencia, o es como determinabilidad frente a otra figura indiferente, o como su naturaleza inorgánica universal. Pero esta naturaleza universal independiente, en la que la negación es como negación absoluta, es el género como tal o como autoconciencia. La autoconciencia sólo alcanza su satisfacción en otra autoconciencia."""
    },
    {
        "id": "ac06",
        "pagina": 112,
        "texto": """Solamente en estos tres momentos se ha cumplido el concepto de la autoconciencia de sí: a) el puro yo no diferenciado es su primer objeto inmediato. b) Pero esta inmediatez es ella misma mediación absoluta, sólo es como superación del objeto independiente, o es la apetencia. La satisfacción de la apetencia es, ciertamente, la reflexión de la autoconciencia en sí misma o la certeza que ha devenido verdad. c) Pero la verdad de esta certeza es más bien la reflexión duplicada, la duplicación de la autoconciencia. Es un objeto para la conciencia, que pone en sí mismo su ser otro o la diferencia como algo nulo, siendo así independiente. La figura diferenciada solamente viva supera indudablemente su propia independencia en el proceso de la vida misma, pero al desaparecer su diferencia también ella deja de ser lo que es; el objeto de la autoconciencia, en cambio, sigue siendo tan independiente en esta negatividad de sí mismo; y, de este modo, es para sí mismo género, fluidez universal en la peculiaridad de su propia distinción; es una autoconciencia viva.

Es una autoconciencia para una autoconciencia. Y solamente así es, en realidad, pues solamente así deviene para ella la unidad de sí misma en su ser otro; el yo, que es el objeto de su concepto, no es en realidad objeto; y solamente el objeto de la apetencia es independiente, pues éste es la sustancia universal inextinguible, la esencia fluida igual a sí misma. En cuanto una autoconciencia es el objeto, éste es tanto yo como objeto. Aquí está presente ya para nosotros el concepto del espíritu. Más tarde vendrá para la conciencia la experiencia de lo que el espíritu es, esta sustancia absoluta que, en la perfecta libertad e independencia de su contraposición, es decir, de distintas conciencias de sí que son para sí, es la unidad de las mismas: el yo es el nosotros y el nosotros el yo. La conciencia sólo tiene en la autoconciencia, como el concepto del espíritu, el punto de viraje a partir del cual se aparta de la apariencia coloreada del más acá sensible y de la noche vacía del más allá suprasensible, para marchar hacia el día espiritual del presente."""
    },
    {
        "id": "ac07",
        "pagina": 113,
        "texto": """A. INDEPENDENCIA Y SUJECION DE LA AUTOCONCIENCIA; SENORIO Y SERVIDUMBRE

La autoconciencia es en y para sí en cuanto que y porque es en sí y para sí para otra autoconciencia; es decir, sólo es en cuanto se la reconoce. El concepto de esta unidad de la autoconciencia es una duplicación, de la infinitud que se realiza en la autoconciencia, es una trabazón multilateral y multivoca, de tal modo que, de una parte, los momentos que aquí se entrelazan deben ser mantenidos rigurosamente separados y, de otra parte, deben ser, al mismo tiempo en esta diferencia, tomados y reconocidos también como momentos que no se distinguen o tomados en esta diferencia, y reconocidos siempre en su significación contrapuesta. El doble sentido de lo diferenciado se halla en la esencia de la autoconciencia que consiste en ser infinita o inmediatamente lo contrario de la determinabilidad en la que es puesta. El desdoblamiento del concepto de esta unidad espiritual en su duplicación presenta ante nosotros el movimiento del reconocimiento.

[1. La autoconciencia duplicada]

Para la autoconciencia hay otra autoconciencia; ésta se presenta fuera de sí. Hay en esto una doble significación; en primer lugar, la autoconciencia se ha perdido a sí misma, pues se encuentra como otra esencia; en segundo lugar, con ello ha superado a lo otro, pues no ve tampoco a lo otro como esencia, sino que se ve a sí misma en lo otro."""
    },
    {
        "id": "ac08",
        "pagina": 114,
        "texto": """Tiene que superar este su ser otro; esto es la superación del primer doble sentido y, por tanto, a su vez, un segundo doble sentido; en primer lugar, debe tender a superar la otra esencia independiente, para de este modo devenir certeza de sí como esencia; y, en segundo lugar, tiende con ello a superarse a sí misma, pues este otro es ella misma.

Esta superación de doble sentido de su ser otro de doble sentido es, igualmente, un retorno a sí misma de doble sentido, pues, en primer lugar, se recobra a sí misma mediante esta superación, pues deviene de nuevo igual a sí por la superación de su ser otro, pero, en segundo lugar, restituye también a sí misma la otra autoconciencia, que era en lo otro, supera este su ser en lo otro y hace, así, que de nuevo libre a lo otro.

Este movimiento de la autoconciencia en su relación con otra autoconciencia se representa, empero, de este modo, como el hacer de la una; pero este hacer de la una tiene él mismo la doble significación de ser tanto su hacer como el hacer de la otra; pues la otra es igualmente independiente, encerrada en sí misma y no hay en ella nada que no sea por ella misma. La primera autoconciencia no tiene ante sí el objeto tal y como este objeto sólo es al principio para la apetencia, sino que tiene ante sí un objeto independiente y que es para sí y sobre el cual la autoconciencia, por tanto, nada puede para sí. Si el objeto no hace en sí mismo lo que ella hace en él. El movimiento es, por tanto, sencillamente el movimiento duplicado de ambas autoconciencias. Cada una de ellas ve a la otra hacer lo mismo que ella hace; cada una hace lo que exige de la otra y, por tanto, sólo hace lo que hace en cuanto la otra hace lo mismo; el hacer unilateral sería ocioso, ya que lo que ha de suceder sólo puede lograrse por la acción de ambas.

El hacer, por tanto, no sólo tiene un doble sentido en cuanto que es un hacer tanto hacia sí como hacia lo otro, sino también en cuanto que ese hacer, como indivisible, es tanto el hacer de lo uno como el de lo otro.

En este movimiento vemos repetirse el proceso que se presentaba como juego de fuerzas, pero ahora en la conciencia. Lo que en el juego de fuerzas era para nosotros es ahora para los extremos mismos. El término medio es la conciencia de sí, que se descompone en los extremos; y cada extremo es este intercambio de su determinabilidad y el tránsito absoluto al extremo opuesto. Pero, como conciencia, aunque cada extremo pase fuera de sí, en su ser fuera de sí es, al mismo tiempo, retenido en sí, es para sí y su fuera de sí es para él. Es para él para lo que es y no es inmediatamente otra con-"""
    },
    {
        "id": "ac09",
        "pagina": 115,
        "texto": """ciencia; y también para él es este otro para sí solamente cuando se supera como lo que es para sí y es para sí solamente en el ser para sí del otro. Cada extremo es para el otro el término medio a través del cual es mediado y unido consigo mismo, y cada uno de ellos es para sí y para el otro una esencia inmediata que es para sí, pero que, al mismo tiempo, sólo es para sí a través de esta mediación. Se reconocen como reconociéndose mutuamente.

Hay que considerar ahora este puro concepto del reconocimiento, de la duplicación de la autoconciencia en su unidad, tal como su proceso aparece para la autoconciencia. Este proceso representará primeramente el lado de la desigualdad de ambas o el desplazamiento del término medio a los extremos, que como extremos se contraponen, siendo el uno sólo lo reconocido y el otro solamente lo que reconoce.

[2. La lucha de las autoconciencias contrapuestas]

La autoconciencia es primeramente simple ser para sí, igual a sí misma, por la exclusión de sí de todo otro; su esencia y su objeto absoluto es para ella el yo; y, en esta inmediatez o en este ser su ser para sí, es singular. Lo que para ella es otro es como objeto no esencial, marcado con el carácter de lo negativo. Pero lo otro es también una autoconciencia; un individuo surge frente a otro individuo. Y, surgiendo así, de un modo inmediato, son el uno para el otro a la manera de objetos comunes; figuras independientes, conciencias hundidas en el ser de la vida —pues como vida se ha determinado aquí el objeto que es—, conciencias que aún no han realizado la una para la otra el movimiento de la abstracción absoluta consistente en aniquilar todo ser inmediato para ser solamente el ser puramente negativo de la conciencia igual a sí misma; o, en otros términos, no se presenta la una con respecto a la otra todavía como puro ser para sí, es decir, como autoconciencias. Cada una de ellas está bien cierta de sí misma, pero no de la otra, por lo que su propia certeza de sí no tiene todavía ninguna verdad, pues su verdad sólo estaría en que su propio ser para sí se presentase ante ella como objeto independiente o, lo que es lo mismo, en que el objeto se presentase como esta pura certeza de sí mismo. Pero, según el concepto del reconocimiento, esto sólo es posible si el otro objeto realiza para él esta pura abstracción del ser para sí, como él para el otro, cada uno en sí mismo, con su propio hacer y, a su vez, con el hacer del otro.

Pero la presentación de sí mismo como pura abstracción de la autoconciencia consiste en mostrarse como pura negación de su modo objetivo o en mostrar que no está vinculado a ningún ser allí determinado, ni a la singularidad universal de la existencia en general, ni se está vinculado a la vida. Esta presentación es el hacer duplicado; hacer del otro y hacer por uno mismo. En cuanto hacer del otro cada cual tiende, pues, a la muerte del otro. Pero en esto se da también el segundo hacer, el hacer por sí mismo, pues aquél entraña el arriesgar la propia vida. Por consiguiente, el comportamiento de las dos autoconciencias se halla determinado de tal modo que se comprueban por sí mismas y la una a la otra mediante la lucha a vida o muerte. Y deben entablar esta lucha, pues deben elevar la certeza de sí misma de ser para sí a la verdad en la otra y en ella misma. Solamente arriesgando la vida se mantiene la libertad, se prueba que la esencia de la autoconciencia no es el ser, no es el modo inmediato como la conciencia de sí surge, ni es su hundirse en la expansión de la vida, sino que en ella no se da nada que no sea para ella un momento que tiende a desaparecer, que la autoconciencia sólo es puro ser para sí. El individuo que no ha arriesgado la vida puede sin duda ser reconocido como persona, pero no ha alcanzado la verdad de este reconocimiento como autoconciencia independiente. Y, del mismo modo, cada cual tiene que tender a la muerte del otro, cuando expone su vida, pues el otro no vale para él más de lo que vale él mismo; su esencia se representa ante él como un otro, se halla fuera de sí y tiene que superar su ser fuera de sí; el otro es una conciencia entorpecida de múltiples modos y que es; y tiene que intuir su ser otro como puro ser para sí o como negación absoluta.

Ahora bien, esta comprobación por medio de la muerte supera precisamente la verdad que de ella debiera surgir, y supera con ello, al mismo tiempo, la certeza de sí misma en general; pues como la vida es la posición natural de la conciencia, la independencia sin la negatividad absoluta, la muerte es la negación natural de la misma conciencia, la negación sin la independencia y que, por tanto, permanece sin la significación postulada del reconocimiento. Por medio de la muerte llega a ser, evidentemente, la certeza de que los dos individuos arriesgaban la vida y la despreciaban cada uno en sí mismo y en el otro, pero no se adquiere para los que afrontan esta lucha. Superan su conciencia puesta en esta esencialidad ajena que es el ser allí natural o se superan a sí mismos, y son superados como extremos que quieren ser para sí. Pero, con ello, desaparece del juego del cambio el momento esencial, consistente en desintegrarse en extremos de determinabilidades contrapuestas; y el término medio coincide con una unidad muerta, que se desintegra en extremos muer-"""
    },
    {
        "id": "ac10",
        "pagina": 116,
        "texto": """tos, que simplemente son y no son contrapuestos; y los dos extremos no se entregan ni se recuperan el uno al otro, mutuamente, por medio de la conciencia, sino que guardan el uno con respecto al otro la libertad de la indiferencia, como cosas. Su hacer es la negación abstracta, no la negación de la conciencia, la cual supera de tal modo que mantiene y conserva lo superado, sobreviviendo con ello a su llegar a ser superada.

En esta experiencia resulta para la autoconciencia que la vida es para ella algo tan esencial como la pura autoconciencia. En la autoconciencia inmediata, el simple yo es el objeto absoluto, pero que es para nosotros o en sí la mediación absoluta y que tiene como momento esencial la independencia subsistente. La disolución de aquella unidad simple es el resultado de la primera experiencia; mediante ella, se ponen una autoconciencia pura y una conciencia, que no es puramente para sí sino para otra, es decir, como conciencia que es o conciencia en la figura de la sociedad. Ambos momentos son esenciales; pero, como son, al comienzo, desiguales y opuestos y su reflexión en la unidad no se ha logrado aún, tenemos que estos dos momentos son como dos figuras contrapuestas de la conciencia: una es la conciencia independiente que tiene por esencia el ser para sí, otra la conciencia dependiente, cuya esencia es la vida o el ser para otro; la primera es el señor, la segunda el siervo.

[3. Señor y siervo]

[a] El señor(a)

El señor es la conciencia que es para sí, pero ya no simplemente el concepto de ella, sino una conciencia que es para sí, que es mediación consigo a través de otra conciencia, a saber: una conciencia a cuya esencia pertenece el estar sintetizada con el ser independiente o la sociedad en general. El señor se relaciona con estos dos momentos: con una cosa como tal, objeto de las apetencias, y con la conciencia para la que la sociedad es lo esencial; y en cuanto que él, el señor, a) como concepto de la autoconciencia, es relación inmediata del ser para sí, pero, al mismo tiempo, b) como mediación o como un ser para sí que sólo es para sí por medio de un otro, se relaciona a) de un modo inmediato, con ambos momentos y b) de un modo mediano, a cada uno de ellos por medio del otro. El señor se relaciona al siervo de un modo mediato, a través del ser independiente, pues a esto precisamente es a lo que se halla sujeto el siervo; ésta es su cadena, de la que..."""
    },
    {
        "id": "ac11",
        "pagina": 117,
        "texto": """...no puede abstraerse en la lucha, y por ella se demuestra como dependiente, como algo que tiene su independencia en la coseidad. Pero el señor es la potencia sobre este ser, pues ha demostrado en la lucha que sólo vale para él como algo negativo; y, al ser la potencia que se halla por encima de este ser y este ser, a su vez, la potencia colocada por encima del otro, así en este silogismo tiene bajo sí a este otro. Y, asimismo, el señor se relaciona con la cosa de un modo mediato, por medio del siervo; el siervo, como autoconciencia en general, se relaciona también de un modo negativo con la cosa y la supera; pero, al mismo tiempo, la cosa es para él algo independiente, por lo cual no puede consumar su destrucción por medio de su negación, sino que se limita a transformarla. Por el contrario, a través de esta mediación la relación inmediata se convierte, para el señor, en la pura negación de la misma o en el goce, lo que la apetencia no lograra lo logra él: acabar con aquello y encontrar satisfacción en el goce. La apetencia no podía lograr esto a causa de la independencia de la cosa; en cambio, el señor, que ha intercalado al siervo entre la cosa y él, no hace con ello más que unirse a la dependencia de la cosa y gozarle puramente; pero abandona el lado de la independencia de la cosa al siervo, que la transforma.

En estos dos momentos deviene para el señor su ser reconocido por medio de otra conciencia; pues ésta se pone en ellos como algo no esencial, de una parte en la transformación de la cosa y, de otra parte, en la dependencia con respecto a una determinada existencia; en ninguno de los dos momentos puede dicha otra conciencia señorear el ser y llegar a la negación absoluta. Se da, pues, aquí, el momento del reconocimiento en que la otra conciencia se supera como ser para sí, haciendo ella misma de este modo lo que la primera hace en contra de ella. Y otro tanto ocurre con el otro momento, en el que esta acción de la segunda es la propia acción de la primera; pues lo que hace el siervo es, propiamente, un acto del señor; solamente para éste es el ser para sí, la esencia; es la pura potencia negativa para la que la cosa no es nada y, por tanto, la acción esencial pura en este comportamiento, y el siervo, por su parte, una acción no pura, sino inesencial. Pero, para el reconocimiento en sentido estricto falta otro momento: el de que lo que el señor hace contra el otro lo haga también contra sí mismo y lo que el siervo hace contra sí lo haga también contra el otro. Se ha producido solamente, por tanto, un reconocimiento unilateral y desigual.

Para el señor, la conciencia no esencial es aquí el objeto, que constituye la verdad de la certeza de sí mismo. Pero, claramente se ve que este objeto no corresponde a su concepto, sino que en aquello en que el señor se ha realizado plenamente deviene para él algo totalmente otro que una conciencia independiente. No es para él una conciencia tal, sino, por el contrario, una conciencia dependiente; el señor no tiene, pues, la certeza del ser para sí como de la verdad, sino que su verdad es, por el contrario, la conciencia no esencial y la acción no esencial de ella.

La verdad de la conciencia independiente es, por tanto, la conciencia serial. Es cierto que ésta comienza apareciendo fuera de sí y no como la verdad de la autoconciencia. Pero, así como el señor revelaba que su esencia es lo inverso de aquello que quiere ser, así también la servidumbre devendrá también, sin duda, al realizarse plenamente lo contrario de lo que de un modo inmediato es; retomará a sí como conciencia respalda sobre sí misma y se convertirá en verdadera independencia."""
    },
    {
        "id": "ac12",
        "pagina": 119,
        "texto": """[b) El temor]

Sólo hemos visto lo que es la servidumbre en el comportamiento del señorío. Pero la servidumbre es autoconciencia, y debemos pararnos a considerar ahora lo que es en y para sí misma. Primeramente, para la servidumbre, el señor es la esencia; por tanto, la verdad es, para ella, la conciencia independiente y que es para sí, pero esta verdad para ella no es todavía en ella. Sin embargo, tiene en ella misma, de hecho, esta verdad de la pura negatividad y del ser para sí, pues ha experimentado en ella misma esta esencia: En efecto, esta conciencia se ha sentido angustiada no por esto o por aquello, no por este o por aquel instante, sino por su esencia entera, pues ha sentido el miedo de la muerte, del señor absoluto. Ello la ha disuelto interiormente, la ha hecho temblar en sí misma y ha hecho estremecerse cuanto había en ella de fijo. Pero este movimiento universal puro, la fluidificación absoluta de toda subsistencia es la esencia simple de la autoconciencia, la absoluta negatividad, el puro ser para sí, que es así en esta conciencia. Este momento del puro ser para sí es también para ella, pues en él señor dicho momento es su objeto. Además, aquella conciencia no es solamente esta disolución universal en general, sino que en el servir la lleva a efecto realmente; al hacerlo, supera en todos los momentos singulares su supeditación a la existencia natural y la elimina por medio del trabajo."""
    },
    {
        "id": "ac13",
        "pagina": 120,
        "texto": """[c) La formación cultural]

Pero el sentimiento de la potencia absoluta en general y en particular el del servicio es solamente la disolución en sí, y aunque el miedo al señor es el comienzo de la sabiduría, la conciencia es en esto para ella misma y no el ser para sí. Pero a través del trabajo llega a sí misma. En el momento que corresponde a la apetencia en la conciencia del señor, parecía tocar a la conciencia servidora el lado de la relación no esencial con la cosa, mientras que ésta mantiene su independencia. La apetencia se reserva aquí la pura negación del objeto y, con ella, el sentimiento de sí mismo sin mezcla alguna. Pero esta satisfacción es precisamente por ello algo que tiende a desaparecer, pues le falta el lado objetivo o la subsistencia. El trabajo, por el contrario, es apetencia reprimida, desaparición contenida, el trabajo formativo. La relación negativa con el objeto se convierte en forma de éste y en algo permanente, precisamente porque ante el trabajador el objeto tiene independencia. Este término medio negativo o la acción formativa es, al mismo tiempo, la singularidad o el puro ser para sí de la conciencia, que ahora se manifiesta en el trabajo fuera de sí y pasa al elemento de la permanencia; la conciencia que trabaja llega, pues, de este modo a la intuición del ser independiente como de sí misma.

Ahora bien, la formación no tiene solamente esta significación positiva de que, gracias a ella, la conciencia servidora se convierte, como puro ser para sí, en lo que es, sino que tiene también una significación negativa con respecto a su primer momento, al temor. En la formación de la cosa, la propia negatividad, su ser para sí, sólo se convierte para ella en objeto en tanto que supera la forma contrapuesta que es. Pero este algo objetivamente negativo es precisamente la esencia extraña ante la que temblaba. Pero, ahora destruye este algo negativo extraño, se pone en cuanto tal en el elemento de lo permanente y se convierte de este modo en algo para sí mismo, en algo que es para sí. En el señor, el ser para sí es para ella un otro o solamente para ella; en el temor, el ser para sí es en ella misma; en la formación, el ser para sí deviene como su propio ser para ella y se revela a la conciencia como es ella misma en y para sí. Por el hecho de colocarse hacia afuera, la forma no se convierte para ella en algo otro que ella, pues esta forma es precisamente su puro ser para sí, que así se convierte para ella en la verdad. Deviene, por tanto, por medio de este reencontrarse por sí misma sentido propio, precisamente en el trabajo, en que sólo parecía ser un sentido extraño. Para esta reflexión son necesarios los dos momentos, tanto el del temor y el del servicio en general como el de la formación, y ambos, de un modo universal. Sin la disciplina del servicio y la obediencia, el temor se mantiene en lo formal y no se propaga a la realidad consciente de la existencia. Sin la formación, el temor permanece interior y mudo y la conciencia no deviene para ella misma. Si la conciencia se forma sin pasar por el temor primario absoluto, sólo es un sentido propio vano, pues su negatividad no es la negatividad en sí, por lo cual su formarse no podrá darle la conciencia de sí como de la esencia. Y si no se ha sobrepuesto al temor absoluto, sino solamente a una angustia cualquiera, la esencia negativa seguirá siendo para ella algo externo, su sustancia no se verá totalmente contaminada por ella. Si todos los contenidos de su conciencia natural no se estremecen, esta conciencia pertenece aún en sí al ser determinado; el sentido propio, es obstinación, una libertad que sigue manteniéndose dentro de la servidumbre. Y, del mismo modo que la pura forma no puede devenir esencia, tampoco esta forma, considerada como expansión más allá de lo singular, puede ser formación universal, concepto absoluto, sino una habilidad capaz de ejercerse sólo sobre algo, pero no sobre la potencia universal y la esencia objetiva total."""
    },
    {
        "id": "ac14",
        "pagina": 122,
        "texto": """B. LIBERTAD DE LA AUTOCONCIENCIA; ESTOICISMO, ESCEPTICISMO Y LA CONCIENCIA DESVENTURADA

[Introducción. La fase de conciencia a que aquí se llega: el pensamiento]

Para la autoconciencia independiente, de una parte, sólo la pura abstracción del yo es su esencia y, de otra parte, al desarrollarse y asumir diferencias esta pura abstracción, este diferenciarse no se convierte para dicha autoconciencia en la esencia objetiva que es en sí; esta autoconciencia no deviene, por tanto, un yo verdaderamente diferenciable en su simplicidad o que en esta diferencia absoluta permanezca igual a sí mismo. Por el contrario, la conciencia repelida sobre sí, se convierte en la formación, como forma de la cosa plasmada, en objeto e intuye en el señor el ser para sí al mismo tiempo como conciencia. Pero ante la conciencia servidora en cuanto tal, estos dos momentos —el de sí misma como objeto independiente y el de este objeto como una conciencia y, por tanto, como su propia esencia— se disocian. Ahora bien, en cuanto que para nosotros o en sí la forma y el ser para sí son lo mismo y en el concepto de la conciencia independiente el ser en sí es la conciencia, tenemos que el lado del ser en sí o de la sociedad, que ha recibido su forma en el trabajo no es otra sustancia que la conciencia y deviene para nosotros en una nueva figura de la autoconciencia; una conciencia que es ante sí la esencia en cuanto la infinitud o el movimiento puro de la conciencia; que piensa o es una autoconciencia libre. Pues pensar se llama a no comportarse como un yo abstracto, sino como un yo que tiene al mismo tiempo el significado del ser en sí, o el comportarse ante la esencia objetiva de modo que ésta tenga el significado del ser para sí de la conciencia para la cual es. Ante el pensamiento el objeto no se mueve en representaciones o en figuras, sino en conceptos, es decir, en un indiferenciado ser en sí que, de modo inmediato para la conciencia, no es diferente de ella. Lo representado, lo configurado, lo que es como tal tienen la forma de ser algo otro que la conciencia; pero un concepto es al mismo tiempo algo que es, y esta diferencia, en cuanto es en la conciencia misma, es su contenido determinado, pero, por el hecho de que este contenido es, al mismo tiempo, concebido conceptualmente permanece inmediatamente consciente de su unidad con este algo que es determinado y diferente y no como en la representación, en la que la conciencia tiene que recordar, además, especialmente que ésta es su representación; el concepto, en cambio, es inmediatamente para mí mi concepto. En el pensamiento yo soy libre, porque no soy en otro, sino que permanezco sencillamente en mí mismo, y el objeto que es para mí la esencia es, en unidad indivisa, mi ser para mí; y mi movimiento en conceptos es un movimiento en mí mismo. Pero en esta determinación de esta figura de la autoconciencia es esencial retener con firmeza que es conciencia pensante en general o que su objeto es la unidad inmediata del ser en sí y del ser para sí. La conciencia homónima consigo misma que de sí misma se repele deviene elemento que es en sí; pero es en este elemento primeramente sólo como esencia universal en general, y no como esta esencia objetiva en el desarrollo y movimiento de su múltiple ser."""
    },
    {
        "id": "ac15",
        "pagina": 123,
        "texto": """[1. El estoicismo]

Como es sabido, esta libertad de la autoconciencia, al surgir en la historia del espíritu como su manifestación consciente, recibió el nombre de estoicismo. Su principio es que la conciencia es esencia pensante y de que algo sólo tiene para ella esencialidad o sólo es para ella verdadero y bueno cuando la conciencia se comporta en ella como esencia pensante.

La múltiple expansión, singularización y complejidad de la vida diferenciada en sí misma es el objeto sobre el que actúan la apetencia y el trabajo. Esta múltiple acción se ha condensado ahora en la simple diferencia que se da en el movimiento puro del pensamiento. No es la diferencia que se manifiesta como cosa determinada o como conciencia de un determinado ser allí natural, como un sentimiento o como apetencia y fin para ella, ya sea puesta por la conciencia propia o por una conciencia ajena, la que tiene más esencialidad, sino solamente la diferencia que es una diferencia pensada o que no se distingue de mí de un modo inmediato. Esta conciencia es, por tanto, negativa ante la relación entre señorío y servidumbre; su acción no es en el señorío tener su verdad en el siervo ni como siervo tener la suya en la voluntad del señor y en el servicio a éste, sino que su acción consiste en ser libre tanto sobre el trono como bajo las cadenas, en toda dependencia de su ser allí singular, en conservar la carencia de vida que constantemente se retrotrae a la esencialidad simple del pensamiento retirándose del movimiento del ser allí, tanto del obrar como del padecer. La obstinación es la libertad que se aferra a lo singular y se mantiene dentro de la servidumbre; el estoicismo, en cambio, la libertad que, escapando siempre inmediatamente a ella, se retrotrae a la pura universalidad del pensamiento; como forma universal del espíritu del mundo, el estoicismo sólo podía surgir en una época de temor y servidumbre universales, pero también de cultura universal, en que la formación se había elevado hasta el plano del pensamiento.

Ahora bien, aunque para esta autoconciencia la esencia no sea ni algo otro que ella ni la pura abstracción del yo, sino el yo que lleva en él el ser otro, pero como diferencia pensada, de tal modo que en su ser otro se ha retrotraído de un modo inmediato a sí mismo, lo cierto es que esta esencia suya sólo es, al mismo tiempo, una esencia abstracta. La libertad de la autoconciencia es indiferente con respecto al ser allí natural, por lo cual ha abandonado también libremente a éste y la reflexión es una reflexión duplicada. La libertad en el pensamiento tiene solamente como su verdad el pensamiento puro, verdad que, así, no aparece llena del contenido de la vida, y es, por tanto, solamente el concepto de la libertad, y no la libertad viva misma, ya que para ella la esencia es solamente el pensamiento en general, la forma como tal, que, al margen de la independencia de las cosas, se ha retrotraído a sí misma. Pero, puesto que la individualidad, como individualidad actuante, debería presentarse como una individualidad viva o, como individualidad pensante, abrazar el mundo vivo como un sistema del pensamiento, tendría necesariamente que encontrarse en el pensamiento mismo para aquella expansión, un contenido de lo que es bueno y para ésta un contenido de lo que es verdadero; para que en lo que es para la conciencia no entre absolutamente ningún otro ingrediente que el concepto, que es la esencia. Pero, como el concepto, en cuanto abstracción, se separa aquí de la multiplicidad de las cosas, no tiene contenido alguno en él mismo, sino un contenido dado. Es cierto que la conciencia cancela el contenido, como un ser ajeno, en tanto que lo piensa; pero el concepto es concepto determinado, y esta determinabilidad del concepto es lo ajeno que tiene en él. De ahí que el estoicismo cayera en la perplejidad cuando se le preguntaba, para emplear la terminología de la época, por el criterio de la verdad en general, es decir, propiamente hablando, por un contenido del pensamiento mismo. Preguntado sobre qué era bueno y verdadero, no daba otra respuesta, una vez más, que el pensamiento mismo sin contenido: lo verdadero y lo bueno debía consistir, según él, en lo racional. Pero esta igualdad del pensamiento consigo mismo no es, a su vez, más que la forma pura en la que nada se determina; de este modo, los términos universales de lo verdadero y lo bueno, de la sabiduría y la virtud, en los que necesariamente tiene que detenerse el estoicismo son también, sin duda, en general, términos edificantes, pero no pueden por menos de engendrar pronto el hastío, ya que en realidad no pueden conducir a una expansión del contenido.

Esta conciencia pensante, tal y como se ha determinado como la libertad abstracta, no es, por tanto, más que la negación imperfecta del ser otro; no habiendo hecho otra cosa que replegarse del ser allí sobre sí misma, no se ha consumado como negación absoluta de la misma. El contenido vale para ella, ciertamente, tan sólo como pensamiento, pero también, al mismo tiempo, como pensamiento determinado y como la determinabilidad en cuanto tal."""
    },
    {
        "id": "ac16",
        "pagina": 125,
        "texto": """[2. El escepticismo]

El escepticismo es la realización de aquello de que el estoicismo era solamente el concepto —y la experiencia real de lo que es la libertad del pensamiento; ésta es en sí lo negativo y tiene necesariamente que presentarse así. Con la reflexión de la autoconciencia en el simple pensamiento de sí misma el ser allí independiente o la determinabilidad permanente se sale con respecto a ella, de hecho, de la infinitud; ahora bien, en el escepticismo devienen para la conciencia la total inesencialidad y falta de independencia de este otro; el pensamiento deviene el pensar completo que destruye el ser del mundo múltiplemente determinado, y la negatividad de la autoconciencia libre se convierte, ante esta múltiple configuración de la vida, en negatividad real. Claramente se ve que así como el estoicismo corresponde al concepto de la conciencia independiente, que se revelaba como la relación entre el señorío y la servidumbre, el escepticismo corresponde a la realización de esta conciencia, como la tendencia negativa ante el ser otro, es decir, a la apetencia y al trabajo. Pero, mientras que la apetencia y el trabajo no podían llevar a término la negación para la autoconciencia, esta tendencia polémica contra la múltiple independencia de las cosas alcanzará, en cambio, su resultado, porque se vuelve en contra de ellas como autoconciencia libre ya previamente lograda; de un modo más preciso, porque esta tendencia lleva en sí misma el pensamiento o la infinitud, por lo cual las independencias, en cuanto a sus diferencias, no son para ella sino magnitudes que tienden a desaparecer. Las diferencias que en el puro pensamiento de sí mismo son solamente la abstracción de las diferencias se convierten, aquí, en todas las diferencias y todo ser distinto se convierte en una diferencia de la autoconciencia.

Hemos determinado así la acción del escepticismo en general y su modo de operar. El escepticismo pone de manifiesto el movimiento dialéctico que son la certeza sensible, la percepción y el entendimiento; y pone de manifiesto, asimismo, la inesencialidad de lo que es válido en la relación entre señorío y servidumbre y de lo que vale como algo determinado para el pensamiento abstracto mismo. Aquella relación entraña al mismo tiempo un determinado modo en el que se dan también preceptos morales como mandamientos del señorío; pero las determinaciones que se dan en el pensamiento abstracto son conceptos de la ciencia, en los que el pensamiento carente de contenido se expande y atribuye el concepto de un modo en realidad puramente externo a un ser independiente de él que constituye su contenido y sólo considera como válidos los conceptos determinados, aunque se trate también de puras abstracciones.

Lo dialéctico, como movimiento negativo, tal y como es de un modo inmediato, empieza revelándose a la conciencia como algo a lo que está entregada y que no es por medio de ella misma. Por el contrario, como escepticismo, dicho movimiento es un momento de la autoconciencia, a quien no accede que desaparezca ante ella, sin que sepa cómo, lo que para ella es lo verdadero y lo real, sino que, en la certeza de su libertad, hace que desaparezca este otro mismo que se presenta como real; no sólo lo objetivo en cuanto tal, sino su propia actitud ante ello, en la que lo objetivo vale y se hace valer en cuanto tal y, por tanto, así su percepción como su consolidación de lo que está en peligro de perder, la sofistaría y lo verdadero determinado y fijado por medio de ella; a través de esta negación autoconsciente, la autoconciencia adquiere para sí misma la certeza de su libertad, hace surgir la experiencia de ella y la eleva de este modo a verdad. Lo que desaparece es lo determinado o la diferencia que, del modo que sea y de donde quiera que venga, se establece como una diferencia firme e inmutable. Semejante diferencia no tiene en sí nada de permanente y tiene necesariamente que desaparecer ante el pensamiento, ya que lo que se diferencia consiste cabalmente en no ser en sí mismo, sino en tener su esencialidad solamente en un otro; el pensamiento, en cambio, es la penetración en esta naturaleza de lo diferente, es la esencia negativa como simple."""
    },
    {
        "id": "ac17",
        "pagina": 127,
        "texto": """Por tanto, la autoconciencia escéptica experimenta en las mutaciones de todo cuanto trata de consolidarse para ella su propia libertad como una libertad que ella misma se ha dado y mantenido; la autoconciencia escéptica es para sí esta ataraxia del pensamiento que se piensa a sí mismo, la inmutable y verdadera certeza de sí misma. Esta certeza no brota de algo ajeno que haga derrumbarse en sí misma su múltiple desarrollo, como un resultado que tuviera tras sí su devenir; sino que la conciencia misma es la inquietud dialéctica absoluta, esa mezcla de representaciones sensibles y pensadas cuyas diferencias coinciden y cuya igualdad se disuelve también de nuevo, ya que es ella misma la determinabilidad con respecto a lo desigual. Pero precisamente por ello, esta conciencia, en realidad, en vez de ser una conciencia igual a sí misma, sólo es una confusión simplemente fortuita, el vértigo de un desorden que se produce constantemente, una y otra vez. Y dicha conciencia es esto para sí misma, pues ella misma mantiene y produce esta confusión en movimiento. Por eso confiesa que es esto, que es una conciencia totalmente contingente y singular, una conciencia que es empírica, que se orienta hacia lo que no tiene para ella ninguna realidad, que obedece a lo que no es para ella esencia alguna, que hace y convierte en realidad lo que no tiene para ella ninguna verdad. Pero, del mismo modo que se hace valer así como una vida singular y contingente, que es, de hecho, vida animal, y autoconciencia perdida, se convierte al mismo tiempo, por el contrario, en autoconciencia universal e igual a sí misma, ya que es la negatividad de todo lo singular y de toda diferencia. De esta igualdad consigo misma o más bien en ella misma recae de nuevo en aquel estado contingente y en aquella confusión, pues precisamente esta negatividad en movimiento sólo tiene que ver con lo singular y se ocupa solamente de lo contingente.

Esta conciencia es, por tanto, ese desatino inconsciente que consiste en pasar a cada paso de un extremo a otro, del extremo de la autoconciencia igual a sí misma al de la conciencia fortuita, confusa y engendradora de confusión, y viceversa. Ella misma no logra aglutinar estos dos pensamientos de ella misma; de una parte, reconoce su libertad como elevación por encima de toda la confusión y el carácter contingente del ser allí y, de otra parte, confiesa ser, a su vez, un retorno a lo no esencial y a un dar vueltas en torno a ello. Hace desaparecer en su pensamiento el contenido no esencial, pero es por ello mismo la conciencia de algo inesencial; proclama la desaparición absoluta, pero esta proclamación es, y esta conciencia es la desaparición proclamada; proclama la nulidad del ver, el oír, etc. y ella misma ve, oye, etc.; proclama la nulidad de las esencialidades éticas y ella misma las erige en potencias de su conducta. Su acción y sus palabras se contradicen siempre y, de este modo, ella misma entraña la conciencia doble y contradictoria de lo inmutable y lo igual y de lo totalmente contingente y desigual consigo misma. Pero mantiene disociada esta contradicción de sí misma y se comporta hacia ella como en su movimiento puramente negativo en general. Si se le indica la igualdad, ella indica la desigualdad; y cuando se le pone delante esta desigualdad, que acaba de proclamarse, ella pasa a la indicación de la igualdad; su charla es, en realidad, una disputa entre muchachos testarudos, uno de los cuales dice A cuando el otro dice B y B si aquél dice A y que, contradiciéndose cada uno de ellos consigo mismo, se dan la satisfacción de permanecer en contradicción el uno con el otro."""
    },
    {
        "id": "ac18",
        "pagina": 128,
        "texto": """En el escepticismo, la conciencia se experimenta en verdad como una conciencia contradictoria en sí misma; y de esta experiencia brota una nueva figura, que aglutina los dos pensamientos manteniendo separados por el escepticismo. La carencia de pensamiento del escepticismo acerca de sí mismo tiene necesariamente que desaparecer, ya que es en realidad una sola conciencia que lleva en sí estos dos modos. Esta nueva figura es, de este modo, una figura tal, que es para sí la conciencia duplicada de sí como conciencia que, de una parte, se libera y es inmutable e idéntica a sí misma y que, de otra parte, es la conciencia de una confusión y una inversión absolutas —y que es así la conciencia de su propia contradicción. En el estoicismo, la autoconciencia es la simple libertad de sí misma; en el escepticismo, esta libertad se realiza, destruye el otro lado del determinado ser allí, pero más bien se duplica y es ahora algo doble. De este modo, la duplicación que antes aparecía repartida entre dos singulares, el señor y el siervo, se resume ahora en uno solo; se hace de este modo presente la duplicación de la autoconciencia en sí misma, que es esencial en el concepto del espíritu, pero aún no su unidad, y la conciencia desventurada es la conciencia de sí como de la esencia duplicada y solamente contradictoria."""
    },
    {
        "id": "ac19",
        "pagina": 129,
        "texto": """[3. La conciencia desventurada. Subjetivismo piadoso]

Esta conciencia desventurada, desdoblada en sí misma, debe ser, por tanto, necesariamente, puesto que esta contradicción de su esencia es para sí una sola conciencia, tener siempre en una conciencia también la otra, por donde se ve expulsada de un modo inmediato de cada una, cuando cree haber llegado al triunfo y a la quietud de la unidad. Pero su verdadero retorno a sí misma o su reconciliación consigo misma se presentará como el concepto del espíritu hecho vivo y entrado en la existencia, porque ya en ella es, como una conciencia indivisa, una conciencia doble; ella misma es la contemplación de una autoconciencia en otra, y ella misma es ambas, y la unidad de ambas es también para ella la esencia; pero, para sí no es todavía esta esencia misma, no es todavía la unidad de ambas.

[a) La conciencia mudable]

Por cuanto que primeramente esa conciencia no es sino la unidad inmediata de ambas, pero de tal modo que no son para ella lo mismo, sino que son contrapuestas, tenemos que la una, la conciencia simple e inmutable, es para ella como la esencia, mientras que la otra, la que cambia de un modo múltiple, es como lo no esencial. Ambas son para ella esencias ajenas la una a la otra; y ella misma, por cuanto que es la conciencia de esta contradicción, se pone del lado de la conciencia cambiante y es para sí lo no esencial; pero, como conciencia de la inmutabilidad o de la esencia simple, tiene necesariamente que proceder, al mismo tiempo, a liberarse de lo inesencial, es decir, a liberarse de sí misma. En efecto, si bien para sí es solamente lo cambiante y lo inmutable es para ella algo ajeno, es ella misma simple y, por tanto, conciencia inmutable, consciente por tanto de ello como de su esencia, pero de tal modo que ella misma no es para sí, a su vez, la esencia. Por consiguiente, la posición que atribuye a las dos no puede ser la de una indiferencia mutua, es decir, la de la indiferencia de ella misma hacia lo inmutable, sino que es de un modo inmediato y ella misma ambas, y para ella la relación entre ambas es como una relación entre la esencia y la no-esencia, de tal modo que esta última es superada; pero,..."""
    },
    {
        "id": "ac20",
        "pagina": 129,
        "texto": """por cuanto que ambas son para ella igualmente esenciales y contradictorias, tenemos que la autoconciencia no es sino el movimiento contradictorio en el que el contrario no llega a la quietud en su contrario, sino que simplemente se engendra de nuevo en él como contrario.

Estamos, por tanto, ante una lucha contra un enemigo frente al cual el triunfar es más bien sucumbir y el alcanzar lo uno es más bien perderlo en su contrario. La conciencia de la vida, de su ser allí y de su acción es solamente el dolor en relación con este ser allí y esta acción, ya que sólo encuentra aquí la conciencia de su contrario como la conciencia de la esencia y de la propia nulidad. Remontándose sobre esto, pasa a lo inmutable. Pero esta elevación es ella misma esta conciencia; es, por tanto, de modo inmediato la conciencia de lo contrario, a saber, la conciencia de sí misma como de lo singular. Y, cabalmente con ello, lo inmutable que entra en la conciencia es tocado al mismo tiempo por lo singular y solamente se presenta con esto; en vez de haberlo extinguido en la conciencia de lo inmutable, se limita a aparecer constantemente de nuevo en ella."""
    },
    {
        "id": "ac21",
        "pagina": 130,
        "texto": """[β] La figura de lo inmutable]

Pero, en este movimiento, experimenta precisamente este surgir de lo singular en lo inmutable y de lo inmutable en lo singular. Para ella, lo singular en general aparece, en la esencia inmutable y, al mismo tiempo, lo singular suyo aparece en aquél. En efecto, la verdad de este movimiento es precisamente el ser uno de esta conciencia duplicada. Pero esta unidad deviene para ella misma primeramente una unidad en la que la diversidad de ambos es todavía lo dominante. De este modo, tenemos que lo singular se presenta para ella vinculado a lo inmutable de tres modos. En primer lugar, ella misma resurge de nuevo como lo opuesto a la esencia inmutable; y se ve retrotraída hasta el comienzo de la lucha, que permanece como el elemento de toda la relación. En segundo lugar, lo inmutable mismo en ella tiene para ella lo singular, de tal modo que es la figura de lo inmutable, a la que se transfiere, así, todo el modo de la existencia. Y, en tercer lugar, ella misma se encuentra como este singular en lo inmutable. El primer inmutable es para ella solamente la esencia ajena que condena lo singular; en cuanto al segundo es una figura de lo singular como ella misma —deviene entonces en tercer lugar hacia el espíritu, tiene la alegría de encontrarse a sí misma en él y adquiere la conciencia de haber reconciliado su singularidad con lo universal.

Lo que aquí se presenta como modo y comportamiento de lo inmutable se ha dado como la experiencia que la autoconciencia desdoblada se forma en su desventura. Esta experiencia no es, ciertamente, su movimiento unilateral, pues es ella misma conciencia inmutable y ésta, con ello y al mismo tiempo, también conciencia singular, y el movimiento, asimismo, movimiento de la conciencia inmutable, que en él se manifiesta lo mismo que el otro, pues este movimiento recorre los siguientes momentos: un primer momento, en el que lo inmutable es lo opuesto a lo singular en general, un segundo momento, en el que lo inmutable, al convertirse por sí mismo en lo singular, se opone al resto de lo singular, y por último un tercer momento, en el que lo inmutable forma una unidad con lo singular. Pero esta consideración, en cuanto nos pertenece a nosotros, es aquí extemporánea, pues hasta ahora sólo hemos visto surgir la inmutabilidad como inmutabilidad de la conciencia, que, por consiguiente, no es la inmutabilidad verdadera, sino la inmutabilidad que lleva todavía en sí una contradicción, no lo inmutable en y para sí mismo; no sabemos, por tanto, cómo esto se comportará. El único resultado a que hemos llegado es que para la conciencia, que es aquí nuestro objeto, estas determinaciones indicadas se manifiestan en lo inmutable."""
    },
    {
        "id": "ac22",
        "pagina": 131,
        "texto": """Esta es la razón de que la conciencia inmutable mantenga también en su configuración misma el carácter y el fundamento del ser desdoblado y del ser para sí con respecto a la conciencia singular. Para ésta es, por tanto, en general, un acaecer el que lo inmutable adquiera la figura de lo singular, del mismo modo que sólo se encuentra contrapuesta a ella, y, por tanto, es por medio de la naturaleza como adquiere esta relación; finalmente, el que se encuentre en él se le revela, en parte, ciertamente, como algo producido por ella misma o por el hecho de ser ella misma singular; pero una parte de esta unidad se le revela como perteneciente a lo inmutable, tanto en cuanto a su origen como en cuanto que ella es; y la contraposición permanece en esta unidad misma. De hecho, mediante la configuración de lo inmutable el momento del más allá no sólo permanece, sino que además se afianza, pues si, por la figura de la realidad singular parece, de una parte, acercarse más a lo inmutable, de otra parte tenemos que lo inmutable es ahora para ella y frente a ella como un uno sensible e impenetrable, con toda la rigidez de algo real; la esperanza de devenir uno con él tiene necesariamente que seguir siendo esperanza, es decir, quedar sin realizarse y sin convertirse en algo presente, pues entre ella y la realización se interpone precisamente la contingencia absoluta o la indiferencia inmóvil que se halla en la configuración misma, en lo que fundamenta a la esperanza. Por la naturaleza de lo uno que es, por la realidad que ha revestido acaece necesariamente que haya desaparecido en el tiempo y que en el espacio se halle lejos y permanezca sencillamente lejos."""
    },
    {
        "id": "ac23",
        "pagina": 132,
        "texto": """[γ] La aglutinación de lo real y la autoconciencia]

Si primeramente el mero concepto de la conciencia desdoblada se determinaba de modo que tendía a la superación de esta conciencia como singular y a su devenir conciencia inmutable, su tendencia se determina ahora en el sentido de superar más bien su relación con el puro inmutable no configurado para relacionarse solamente con lo inmutable configurado. En efecto, el ser uno de lo singular con lo inmutable es para él, en adelante, esencia y objeto, mientras que en el concepto su objeto esencial era solamente lo inmutable abstracto y no configurado; y aquello de que ahora tiene que apartarse es la actitud de este desdoblamiento absoluto del concepto. Y debe elevar al devenir uno absoluto su relación primeramente externa con lo inmutable configurado como una realidad ajena.

El movimiento mediante el cual la conciencia no esencial tiende a alcanzar este ser uno es él mismo un movimiento triple, a tono con la triple actitud que habrá de adoptar ante su más allá configurado: de una parte, como conciencia pura; de otra parte, como esencia singular que se comporta hacia la realidad como apetencia y como trabajo, en tercer lugar, como conciencia de su ser para sí. Cómo estos tres modos de su ser se hallan presentes y se determinan en aquella relación general es lo que ahora hay que ver.

[1. La conciencia pura, el ánimo, el fervor] Si, por tanto se considera primeramente esta conciencia como conciencia pura parece como si lo inmutable configurado en tanto que es para la conciencia pura se pusiera como es en sí y para sí mismo. Sin embargo, el cómo es en sí y para sí mismo es, como ya hemos señalado, algo que aún no ha nacido. Para que fuese en la conciencia tal y como es en y para sí mismo tendría, evidentemente, que partir más bien de él que de la conciencia; pero esta su presencia aquí sólo se da todavía de un modo unilateral a través de la conciencia, lo que hace precisamente que no exista de un modo perfecto y verdadero, sino que permanezca afectado de imperfección o de una contraposición.

Por tanto, aunque la conciencia desventurada no posea esta pre-"""
    },
    {
        "id": "ac24",
        "pagina": 133,
        "texto": """sencia de su más allá ideal pensado, tiene, sin embargo, su más allá en cuanto lo piensa, como un más allá sensible; pero al mismo tiempo lo ha retirado de la indeterminación del pensar y lo ha determinado como un ser sensible, y así ha devuelto el pensamiento al tiempo, fijándolo como una realidad puramente efímera y en el espacio como una realidad lejana. El modo y la manera en que en este conflicto la conciencia es y se comporta, manteniendo ambos lados, por una parte como pura conciencia, contrapuesta a la conciencia real y, por otra parte, como conciencia real, contrapuesta a su hacer y a su gozar, y, en tercer lugar, como conciencia de su ser para sí, contrapuesta a la conciencia universal, todo esto tenemos que verlo ahora en el curso de su movimiento."""
    },
    {
        "id": "ac25",
        "pagina": 134,
        "texto": """Esta relación mediata es, por tanto, un silogismo en el que la singularidad, que empieza fijándose como opuesta al en sí, sólo se halla en conexión con este otro extremo por medio de un tercer término. A través de este término medio, es para la conciencia inesencial el extremo de la conciencia inmutable, y esta conciencia inesencial, a su vez, sólo puede ser para la conciencia inmutable a través de este término medio; por donde éste es, así, un término medio que representa a ambos extremos, el uno frente al otro, y el mutuo servidor de cada uno de ellos cerca del otro. Este término medio es él mismo una esencia consciente, ya que es una acción que sirve de mediadora a la conciencia como tal; el contenido de esta acción es la cancelación que la conciencia lleva a cabo de su singularidad.

En él, la conciencia se libera, por tanto, de la acción y el goce como de lo suyo: repudia de sí misma como extremo que es para sí la esencia de su voluntad y arroja sobre el término medio o el servidor la peculiaridad y la libertad de la decisión y, con ello, la culpa de lo que hace. Este mediador, que se halla en relación inmediata con la esencia inmutable, sirve como consejero acerca de lo que es justo. La acción, en cuanto acatamiento de una decisión ajena, deja de ser una acción propia, en lo tocante al lado de la acción o de la voluntad. Pero para la conciencia inesencial permanece aún su lado objetivo, a saber, el fruto de su trabajo y el disfrute. También esto es repudiado de sí misma por ella y, del mismo modo que renuncia a su voluntad, renuncia también a su realidad lograda en el trabajo y en el disfrute; renuncia a ella, en parte como a la verdad alcanzada de su independencia autoconsciente —en cuanto se mueve como algo totalmente ajeno, que le sugiere la representación y le habla en el lenguaje de lo que carece de sentido— y, en parte, como propiedad externa, al ceder algo de la posesión adquirida por medio del trabajo y, en parte, finalmente, renuncia al goce ya logrado, al prohibírselo totalmente de nuevo la abstinencia y la mortificación.

A través de estos momentos, primero el de la renuncia a su propia decisión, luego de la renuncia a la propiedad y al goce y, por último, el momento positivo de la realización de algo que no comprende, se priva en verdad y plenamente de la conciencia de la libertad interior y exterior, de la realidad como su ser para sí; tiene la certeza de haberse enajenado en verdad de su yo, y de haber convertido su autoconciencia inmediata en una cosa, en un ser objetivo."""
    },
    {
        "id": "ac26",
        "pagina": 135,
        "texto": """el goce; la segunda es esta realización, como acción y goce externos; pero, al retomar de ella, la conciencia se ha experimentado como una conciencia real y actuante o como conciencia cuya verdad es ser en y para sí. Pero, aquí se descubre ahora al enemigo bajo su figura más peculiar. En la lucha del ánimo la conciencia singular es solamente como momento musical, abstracto; en el trabajo y el goce, como la realización [Realisierung] de este ser carente de esencia, puede olvidarse de un modo inmediato y la peculiaridad consciente que reside en esta realidad es echada a tierra por el reconocimiento agradecido. Pero este echar por tierra es, en verdad, un retorno de la conciencia a sí misma y, concretamente, a sí misma como a la verdadera realidad.

Esta tercera actitud, en la que esta verdadera realidad es uno de los extremos, es la relación de esa realidad con la esencia universal como la nada; y el movimiento de esta relación es el que vamos ahora a considerar.

Por lo que se refiere, en primer lugar, a la relación contrapuesta de la conciencia, en la que su realidad es para ella inmediatamente lo nulo, vemos que su acción real deviene, por tanto, una acción de nada y su goce deviene el sentimiento de su desventura. De este modo, la acción y el goce pierden todo contenido y toda significación universales, ya que de otro modo tendrían un ser en y para sí, y ambos se retrotraen a la singularidad, hacia la que tiende la conciencia, para superarla. En las funciones animales la conciencia es consciente de sí como de este singular real. Estas funciones, en vez de cumplirse espontáneamente, como algo nulo en y para sí y que no puede alcanzar importancia ni esencialidad alguna para el espíritu, como son funciones en las que el enemigo se manifiesta bajo su figura peculiar, constituyen más bien objeto de serio esfuerzo y se convierten precisamente en lo más importante. Pero, como este enemigo se produce en su derrota, la conciencia, al fijarlo, en vez de ser liberada de él, permanece siempre en relación con él y se siente siempre maculada, y, al mismo tiempo, este contenido de sus aspiraciones, en vez de ser algo esencial, es lo más vil y, en vez de ser algo universal, es lo más singular, y así, vemos nosotros solamente a una personalidad limitada a sí misma y a su pequeña acción y entregada a ella, una personalidad tan desventurada como pobre.

Pero, en ambos casos, al sentimiento de su desventura y a la pobreza de su acción va unida también la conciencia de su unidad con lo inmutable. Pues el intento de la anulación inmediata de su ser real se lleva a cabo por mediación del pensamiento de lo inmutable y acaece en esta relación. La relación mediata constituye la esencia..."""
    },
    {
        "id": "ac27",
        "pagina": 136,
        "texto": """...como la cual aparece en la actividad es el más allá de sí misma. Por tanto, en vez de retomar a sí desde su acción y de haberse probado a sí por sí misma, lo que hace es reflejar este movimiento de la acción en el otro extremo, que se presenta de este modo como puro universal, como la potencia absoluta de que arranca el movimiento hacia todos los lados y que es tanto la esencia de los extremos que se desintegran, en su manera primitiva de presentarse, como la esencia del cambio mismo.

Cuando la conciencia inmutable renuncia a su figura y la abandona y, frente a ello, la conciencia individual da gracias, es decir, se niega la satisfacción de la conciencia de su independencia y transfiere de sí al más allá la esencia de la acción, cuando se dan estos dos momento de la entrega mutua de ambas partes, con ello nace, ciertamente, para la conciencia su unidad con lo inmutable. Pero, al mismo tiempo, esta unidad es afectada por la separación, de nuevo rota en sí y surge nuevamente de ella la oposición de lo universal y lo singular. La conciencia, aunque renuncie a la apariencia de la satisfacción de su sentimiento de sí misma, adquiere, sin embargo, la real satisfacción de este sentimiento, ya que ella ha sido apetencia, trabajo y goce: como conciencia, ha querido, ha hecho y ha gozado. Y su gratitud, con la que reconoce al otro extremo como la esencia y se supera, es también su propia acción, que contrapresta la del otro extremo y opone al beneficio que se abandona una acción igual; si aquel extremo le cede algo superficial de sí mismo, la conciencia da gracias también y, con ello, al renunciar, a su propia acción, es decir, a su esencia misma, hace propiamente más que el otro, que se limita a ceder de sí algo superficial. Por tanto, no solamente en la apetencia, el trabajo y el goce reales, sino también incluso en la misma gratitud, en la que parece suceder lo contrario, y el movimiento en su totalidad se refleja en el extremo de la singularidad. La conciencia se siente aquí como este singular y no se deja engañar por la apariencia de su renuncia, pues la verdad de ella reside en no haberse entregado; lo que se ha producido es solamente la doble reflexión en los dos extremos, y el resultado es la escisión repetida en la conciencia contrapuesta de lo inmutable y en la conciencia del querer, el realizar y el gozar contrapuestos y de la renuncia a sí misma de la singularidad que es para sí, en general.

[3. La autoconciencia que arriba a la razón. (La mortificación de sí mismo)] Se produce así la tercera actitud del movimiento de esta conciencia, que surge de la segunda, en la que la conciencia se ha probado en verdad como independiente por medio de su querer y su realizar. En la primera actitud era solamente el concepto de la conciencia real o el ánimo interior, todavía no real en la acción y..."""
    },
    {
        "id": "ac28",
        "pagina": 137,
        "texto": """...esta seguridad, de tal modo que, aun encontrando en ella dicha seguridad, sólo será la seguridad de lo que ella es para sí, es decir, de su desdoblamiento.

La realidad contra la que se vuelven la apetencia y el trabajo no es ya, para esta conciencia, algo nulo en sí, algo que ella haya simplemente de superar y devorar, sino algo como ella misma es: una realidad rota en dos, que solamente de una parte es nula en sí, mientras que de otra parte es un mundo sagrado; es la figura de lo inmutable, pues esto ha conservado en sí la singularidad y, por ser universal en cuanto inmutable, su singularidad tiene en general la significación de toda la realidad.

Si la conciencia fuese conciencia para sí independiente y la realidad, para ella, algo nulo en y para sí, llegaría en el trabajo y en el goce al sentimiento de su independencia, por cuanto que sería ella misma la que superaría la realidad. Sin embargo, siendo ésta para ella la figura de lo inmutable, no puede superarlo por sí sola, sino que, cuando en verdad llega a la anulación de la realidad y al goce, esto sólo sucede para ella, esencialmente, porque lo inmutable mismo abandona su figura y se la cede para que la goce. A su vez, la conciencia surge aquí, asimismo, como real, pero como algo también interiormente roto, y este desdoblamiento se presenta en su trabajo y en su goce, en desdoblarse en una actitud ante la realidad o el ser para sí y en un ser en sí. Aquella actitud ante la realidad es el alterar o el actuar, el ser para sí, que corresponde a la conciencia singular como tal. Pero en ello es también en sí: este lado pertenece al más allá inmutable; está formado por las capacidades y las fuerzas, un don ajeno que lo inmutable cede también a la conciencia para usarlo.

Por tanto, en su actuación, la conciencia es, por el momento, la relación entre dos extremos; se mantiene, de una parte, como el más acá activo y frente a ella aparece la realidad pasiva, ambas en relación con la una con la otra, pero ambas también retrotraídas a lo inmutable y aferradas a sí. De ambos lados se desprende, por consiguiente, tan sólo algo superficial que se enfrenta al otro en el juego del movimiento. El extremo de la realidad es superado por el extremo activo; pero ella, por su parte, sólo puede ser superada porque su esencia inmutable la supera ella misma, se repele de sí y abandona lo repelido a la actividad. La fuerza activa se manifiesta como la potencia en que se disuelve la realidad; pero, por ello, para esta conciencia, para la que el en sí o la esencia es un otro, esta potencia como la cual aparece en la actividad es el más allá de sí misma. Por tanto, en vez de retomar a sí desde su acción y de haberse probado..."""
    },
    {
        "id": "ac29",
        "pagina": 138,
        "texto": """...tado la esencia sólo ha captado lo inesencial. Y así como, de una parte, al tratar de captarse a sí en la esencia, sólo capta la propia realidad desdoblada, no puede tampoco, de otra parte, captar lo otro como singular o como real. No se lo encontrará dondequiera que se le busque, precisamente porque tiene que ser un más allá, un ser tal que no puede ser encontrado. Buscado como singular, no es una singularidad universal pensada, no es concepto, sino un singular como objeto o algo real; objeto de la certeza sensible inmediata y, precisamente por ello, solamente un objeto que ya ha desaparecido. Ante la conciencia sólo se hace presente, por tanto, el sepulcro de su vida. Pero, como este mismo es una realidad y va contra la naturaleza de la realidad el garantizar una posesión permanente, tampoco la presencia del sepulcro es otra cosa que la lucha de un esfuerzo condenado necesariamente a frustrarse. Sin embargo, al pasar por la experiencia de que el sepulcro de su esencia real e inmutable carece de realidad, de que la singularidad desaparecida, como desaparecida, no es la verdadera singularidad, renunciará a indagar la singularidad inmutable como real o a retenerla como desaparecida, y solamente así será capaz de encontrar la singularidad como verdadera o como universal.

[2. La esencia singular y la realidad. El obrar de la conciencia piadosa] Pero, ante todo, debemos tomar el retorno del ánimo a sí mismo de tal modo que es como un singular que tiene realidad. Es el puro ánimo el que se ha encontrado para nosotros o en sí y se ha satisfecho en sí mismo, pues aunque para él, en su sentimiento, la esencia se separe de él, en sí este sentimiento es sentimiento de sí mismo, ha sentido el objeto de su puro sentir y él mismo es este objeto; surge, pues, de esto como sentimiento de sí mismo o como algo real que es para sí. En este retorno a sí mismo deviene para nosotros su segunda actitud, la actitud de la apetencia y el trabajo, que confiere a la conciencia la certeza interior de sí misma, certeza que ha adquirido para nosotros, y se la confiere mediante la superación y el goce de la esencia ajena, o sea de la esencia bajo la forma de las cosas independientes. Pero la conciencia desventurada sólo se encuentra como conciencia apetente y laboriosa; no advierte que para encontrarse así tiene que basarse en la certeza interior de sí misma y que su sentimiento de la esencia es este sentimiento de sí misma. Y, en cuanto no tiene para sí misma esta certeza, su interior sigue siendo más bien la certeza rota de sí misma; por tanto, la seguridad que adquiriría mediante el trabajo y el goce es también una seguridad rota; o más bien diríamos que ella misma destruiría esta seguridad, de tal modo que, aun encontrando en ella dicha seguridad, sólo será la seguridad de lo que ella es para sí, es decir, de su desdoblamiento..."""
    },
    {
        "id": "ac30",
        "pagina": 139,
        "texto": """...en general. Pero, para ella misma permanece la acción y su acción real una acción misera, su goce el dolor y la superación de este dolor, en su significación positiva, un más allá. Pero, en este objeto, en el que su acción y su ser, como ser y acción de esta conciencia singular son para ella ser y acción en sí, deviene para ella la representación de la razón, de la certeza de la conciencia de ser, en su singularidad, absoluta en sí o toda realidad."""
    }
]

# Notas de análisis del Capítulo IV
NOTAS_AUTOCONCIENCIA = {
    "ac01": "Fragmento ac01 (p107): Introducción a la autoconciencia; la certeza es igual a su verdad; el yo como contenido y relación.",
    "ac02": "Fragmento ac02 (p107-108): La autoconciencia en sí; reflexión desde el ser otro; la autoconciencia como apetencia.",
    "ac03": "Fragmento ac03 (p108-109): La vida como objeto; la vida es infinitud, proceso de figuras independientes; determinación de la vida.",
    "ac04": "Fragmento ac04 (p110): La vida como proceso; devorar lo universal; el ciclo de la vida: configuración y superación.",
    "ac05": "Fragmento ac05 (p111-112): El yo y la apetencia; la autoconciencia como género; la apetencia aniquila el objeto pero la satisfacción es momentánea; la autoconciencia solo alcanza satisfacción en otra autoconciencia.",
    "ac06": "Fragmento ac06 (p112-113): Los tres momentos de la autoconciencia; la autoconciencia para otra autoconciencia; concepto del espíritu.",
    "ac07": "Fragmento ac07 (p113): Introducción a la independencia y sujeción; el movimiento del reconocimiento; la autoconciencia duplicada.",
    "ac08": "Fragmento ac08 (p114): La superación de doble sentido; el hacer duplicado; comparación con el juego de fuerzas.",
    "ac09": "Fragmento ac09 (p115): El concepto del reconocimiento; la lucha a muerte; necesidad de arriesgar la vida.",
    "ac10": "Fragmento ac10 (p116): La negación abstracta de la muerte; surgimiento del señor y el siervo; el señor como conciencia para sí mediada por el siervo.",
    "ac11": "Fragmento ac11 (p117-118): Desarrollo del señorío; el señor goza a través del trabajo del siervo; reconocimiento unilateral; la verdad del señorío está en la conciencia servil.",
    "ac12": "Fragmento ac12 (p119): El temor a la muerte disuelve al siervo y lo abre a la negatividad; el miedo al señor absoluto es el comienzo de la sabiduría.",
    "ac13": "Fragmento ac13 (p120-121): El trabajo como apetencia reprimida y formación (Bildung); el siervo se reconoce en el producto; necesidad del temor y la formación para la verdadera independencia.",
    "ac14": "Fragmento ac14 (p122-123): Introducción a la libertad de la autoconciencia; el pensamiento como nueva figura; el concepto y la libertad en el pensar.",
    "ac15": "Fragmento ac15 (p123-124): El estoicismo: libertad abstracta en el pensamiento; indiferencia ante la existencia; carencia de contenido.",
    "ac16": "Fragmento ac16 (p125-126): El escepticismo como realización de la libertad; negación de todo ser otro; movimiento dialéctico.",
    "ac17": "Fragmento ac17 (p127-128): La autoconciencia escéptica; ataraxia y contradicción; la conciencia como confusión y desatino.",
    "ac18": "Fragmento ac18 (p128-129): Del escepticismo a la conciencia desventurada; duplicación de la autoconciencia en una sola.",
    "ac19": "Fragmento ac19 (p129): La conciencia desventurada; desdoblamiento en inmutable y mudable; contradicción interna.",
    "ac20": "Fragmento ac20 (p129-130): La lucha contra el enemigo interior; el dolor y la elevación a lo inmutable; lo inmutable es tocado por lo singular.",
    "ac21": "Fragmento ac21 (p130-131): Las tres figuras de lo inmutable en la conciencia desventurada; la experiencia de la duplicación.",
    "ac22": "Fragmento ac22 (p131-132): La configuración de lo inmutable y la persistencia del más allá; la esperanza irrealizable.",
    "ac23": "Fragmento ac23 (p132-133): La tendencia a lo inmutable configurado; las tres actitudes de la conciencia (pura, real, ser para sí).",
    "ac24": "Fragmento ac24 (p133): La conciencia desventurada y su más allá sensible; el conflicto y las tres formas de conciencia.",
    "ac25": "Fragmento ac25 (p134): El silogismo de la conciencia desventurada; el mediador; la renuncia a la decisión, propiedad y goce; la enajenación del yo en cosa.",
    "ac26": "Fragmento ac26 (p135): La tercera actitud; la realidad como nada; las funciones animales; la personalidad desventurada y pobre.",
    "ac27": "Fragmento ac27 (p136): La gratitud y la unidad rota; la tercera actitud: la mortificación de sí mismo.",
    "ac28": "Fragmento ac28 (p137): La realidad como figura de lo inmutable; el trabajo y el goce como don; la potencia activa como más allá.",
    "ac29": "Fragmento ac29 (p138): El sepulcro y la búsqueda fallida; el retorno del ánimo; la certeza rota.",
    "ac30": "Fragmento ac30 (p139): La acción misera y el dolor; la representación de la razón; tránsito a la Razón."
}

# Ejemplos concretos del Capítulo IV
EJEMPLOS_AUTOCONCIENCIA = {
    "ac03": [{"tipo": "vida", "descripcion": "La vida como proceso infinito, fluidez universal, figuras independientes que se devoran"}],
    "ac05": [{"tipo": "apetencia", "descripcion": "La autoconciencia como apetencia que aniquila el objeto independiente pero lo reproduce"}],
    "ac06": [{"tipo": "autoconciencia duplicada", "descripcion": "Una autoconciencia para otra autoconciencia; el yo que es nosotros"}],
    "ac07": [{"tipo": "reconocimiento", "descripcion": "La autoconciencia se pierde y se encuentra en otra; doble significación"}],
    "ac08": [{"tipo": "hacer duplicado", "descripcion": "El hacer de cada autoconciencia es también el hacer de la otra; acción recíproca"}],
    "ac09": [{"tipo": "lucha a muerte", "descripcion": "Las autoconciencias luchan a muerte para probar su ser para sí"}],
    "ac10": [{"tipo": "señor y siervo", "descripcion": "El señor es la conciencia independiente; el siervo la dependiente"}],
    "ac11": [{"tipo": "reconocimiento unilateral", "descripcion": "El señor es reconocido por el siervo, pero no reconoce al siervo; el reconocimiento es desigual."}],
    "ac12": [{"tipo": "temor", "descripcion": "El miedo a la muerte, al señor absoluto, disuelve al siervo y lo prepara para la verdadera independencia."}],
    "ac13": [{"tipo": "trabajo formativo", "descripcion": "El trabajo como apetencia reprimida que da forma permanente al objeto; el siervo se reconoce en su producto."}],
    "ac14": [{"tipo": "pensamiento", "descripcion": "La autoconciencia libre que se mueve en conceptos; el yo que es en sí y para sí."}],
    "ac15": [{"tipo": "estoicismo", "descripcion": "Libertad abstracta; el sabio es libre incluso en cadenas."}],
    "ac16": [{"tipo": "escepticismo", "descripcion": "Negación de toda verdad; la conciencia como inquietud dialéctica."}],
    "ac17": [{"tipo": "ataraxia", "descripcion": "La imperturbabilidad del escéptico, pero también su contradicción interna."}],
    "ac18": [{"tipo": "conciencia desventurada", "descripcion": "La duplicación de la autoconciencia en una sola; la contradicción no resuelta."}],
    "ac19": [{"tipo": "inmutable y mudable", "descripcion": "La conciencia desventurada se escinde entre una esencia inmutable (Dios) y su propio ser mudable."}],
    "ac20": [{"tipo": "lucha interior", "descripcion": "La conciencia desventurada lucha contra un enemigo que es ella misma; triunfar es sucumbir."}],
    "ac21": [{"tipo": "tres figuras de lo inmutable", "descripcion": "Lo inmutable como esencia ajena, como figura singular, y como unidad reconciliada."}],
    "ac22": [{"tipo": "esperanza irrealizable", "descripcion": "La configuración de lo inmutable hace que la unión sea siempre lejana e inalcanzable."}],
    "ac23": [{"tipo": "tres actitudes", "descripcion": "Conciencia pura, conciencia real (apetencia y trabajo), y conciencia de sí."}],
    "ac24": [{"tipo": "más allá sensible", "descripcion": "Lo inmutable pensado como un objeto sensible lejano en tiempo y espacio."}],
    "ac25": [{"tipo": "silogismo de la conciencia desventurada", "descripcion": "El mediador (clérigo, sacerdote) que conecta la conciencia singular con lo inmutable mediante la renuncia."}],
    "ac26": [{"tipo": "funciones animales", "descripcion": "La conciencia desventurada se fija en lo más vil y singular, como las funciones corporales, convirtiéndolas en objeto de esfuerzo."}],
    "ac27": [{"tipo": "mortificación", "descripcion": "La tercera actitud: la conciencia se mortifica a sí misma para alcanzar lo inmutable."}],
    "ac28": [{"tipo": "don de lo inmutable", "descripcion": "Las capacidades y fuerzas son un don ajeno que lo inmutable cede a la conciencia."}],
    "ac29": [{"tipo": "sepulcro", "descripcion": "La búsqueda de lo inmutable como realidad singular termina en el sepulcro vacío."}],
    "ac30": [{"tipo": "representación de la razón", "descripcion": "La conciencia alcanza la certeza de ser, en su singularidad, absoluta en sí o toda realidad; tránsito a la Razón."}]
}

# Momentos dialécticos del Capítulo IV
MOMENTOS_AUTOCONCIENCIA = [
    "transición desde el entendimiento",
    "la autoconciencia como certeza de sí",
    "reflexión desde el ser otro",
    "la autoconciencia como apetencia",
    "la vida como objeto",
    "la vida como infinitud",
    "la vida como proceso: figuras independientes",
    "devorar lo universal",
    "el ciclo de la vida",
    "el yo como género",
    "la apetencia y su satisfacción",
    "la insatisfacción de la apetencia",
    "la autoconciencia solo alcanza satisfacción en otra",
    "los tres momentos de la autoconciencia",
    "el concepto del espíritu",
    "el reconocimiento",
    "la autoconciencia duplicada",
    "el hacer duplicado",
    "la lucha a muerte",
    "el riesgo de la vida",
    "la negación abstracta de la muerte",
    "el surgimiento del señor y el siervo",
    "el señor como conciencia para sí",
    "el señor goza a través del trabajo del siervo",
    "reconocimiento unilateral",
    "la verdad del señorío está en el siervo",
    "el temor a la muerte",
    "el trabajo como formación (Bildung)",
    "el siervo se reconoce en el producto",
    "necesidad del temor y la formación",
    "el pensamiento como nueva figura",
    "la libertad en el pensamiento",
    "estoicismo: libertad abstracta",
    "carencia de contenido del estoicismo",
    "escepticismo: negación de todo ser otro",
    "la conciencia escéptica como inquietud",
    "ataraxia y contradicción",
    "la disputa de los muchachos testarudos",
    "duplicación de la autoconciencia en una sola",
    "conciencia desventurada",
    "escisión en inmutable y mudable",
    "la lucha interior de la conciencia desventurada",
    "el dolor y la elevación a lo inmutable",
    "las tres figuras de lo inmutable",
    "la experiencia de la duplicación",
    "la configuración de lo inmutable",
    "la esperanza irrealizable",
    "el más allá sensible",
    "las tres actitudes de la conciencia",
    "conciencia pura, real y para sí",
    "el conflicto de la conciencia desventurada",
    "el silogismo de la conciencia desventurada",
    "el mediador",
    "la renuncia a la decisión",
    "la renuncia a la propiedad",
    "la renuncia al goce",
    "la enajenación del yo en cosa",
    "la tercera actitud",
    "la realidad como nada",
    "las funciones animales",
    "la personalidad desventurada",
    "la gratitud y la unidad rota",
    "la mortificación de sí mismo",
    "la realidad como figura de lo inmutable",
    "el trabajo y el goce como don",
    "la potencia activa como más allá",
    "el sepulcro",
    "la búsqueda fallida",
    "el retorno del ánimo",
    "la certeza rota",
    "la acción misera",
    "la representación de la razón",
    "tránsito a la Razón"
]

# Metáforas clave del Capítulo IV
METAFORAS_AUTOCONCIENCIA = [
    "autoconciencia", "certeza de sí", "reflexión", "apetencia", "vida", "infinitud",
    "fluidez", "figura", "independiente", "universal", "devorar", "proceso",
    "género", "yo puro", "objeto", "satisfacción", "aniquilar", "reproducir",
    "otra autoconciencia", "espíritu", "nosotros", "reconocimiento", "duplicación",
    "hacer duplicado", "lucha a muerte", "riesgo", "negación abstracta", "señor",
    "siervo", "cadena", "cosa", "apetencia", "ser para sí", "ser para otro",
    "temor", "muerte", "señor absoluto", "disolución", "trabajo", "formación",
    "Bildung", "sentido propio", "obstinación", "pensamiento", "concepto",
    "libertad abstracta", "estoicismo", "escepticismo", "ataraxia", "inquietud dialéctica",
    "vértigo", "desatino", "conciencia desventurada", "inmutable", "mudable",
    "lucha interior", "enemigo", "dolor", "elevación", "esperanza", "más allá",
    "conciencia pura", "fervor", "conflicto", "silogismo", "mediador", "renuncia",
    "enajenación", "mortificación", "función animal", "sepulcro", "ánimo",
    "gratitud", "don", "potencia", "acción misera", "razón", "toda realidad"
]

# -------------------------------------------------------------------
# DATOS DEL CAPÍTULO V (FRAGMENTOS COMPLETOS)
# -------------------------------------------------------------------

FRAGMENTOS_CAPITULO5 = [
    {
        "id": "r01",
        "pagina": 143,
        "texto": """V. CERTEZA Y VERDAD DE LA RAZÓN

En el pensamiento captado por ella de que la conciencia singular es en sí esencia absoluta, la conciencia retorna a sí misma. Para la conciencia desventurada, el ser en sí es el más allá de sí misma. Pero su movimiento la ha llevado al siguiente resultado: la singularidad, en su desarrollo total, o la singularidad que es conciencia real, ha sido puesta como lo negativo de sí misma, es decir, como el extremo objetivo o ha desgajado de sí su ser para sí, convirtiéndolo en el ser; de este modo, ha devenido también para la conciencia su unidad con este universal que, para nosotros, no cae ya fuera de ella, puesto que lo singular superado es lo universal; y, como la conciencia se mantiene a sí misma en esta su negatividad, su esencia es en ella como tal. Su verdad es aquello que en el silogismo, en el que los extremos aparecían absolutamente disociados, se manifestaba como el término medio que anuncia a la conciencia inmutable que lo singular ha renunciado a sí y a lo singular que lo inmutable no es ya un extremo para él, sino que se ha reconciliado con él. Este término medio es la unidad que encierra un saber inmediato de ambos y los relaciona entre sí y la conciencia de su unidad que anuncia a la conciencia, y con ello se anuncia a sí misma la certeza de ser toda verdad."""
    },
    {
        "id": "r02",
        "pagina": 143,
        "texto": """Por cuanto que la autoconciencia es razón, su actitud hasta ahora negativa ante el ser otro se trueca en una actitud positiva. Hasta ahora, sólo le preocupaban su independencia y su libertad, para salvarse y mantenerse para sí misma a costa del mundo o de su propia realidad, ya que ambos se le manifestaban como lo negativo de su esencia. Pero, como razón, segura ya de sí misma, se pone en paz con el mundo y con su propia realidad y puede soportarlos, pues ahora tiene la certeza de sí misma como de la realidad o la certeza de que toda realidad no es otra cosa que ella; su pensamiento mismo es, de un modo inmediato, la realidad; se comporta, pues, hacia ella como idealismo. Para ella, al captarse así, es como si el mundo deviniese por vez primera; antes, no lo comprendía; lo apetecía y lo elaboraba, se replegaba de él sobre sí misma, lo cancelaba para sí y se cancelaba a sí misma como conciencia, como conciencia del mundo en tanto que conciencia de la esencia, lo mismo que como conciencia de su nulidad. Solamente ahora, después de haber perdido el sepulcro de su verdad, después de haber cancelado la cancelación misma de su realidad y cuando ya la singularidad de la conciencia es para ella en sí la esencia absoluta, descubre la conciencia el mundo como su nuevo mundo real, que ahora le interesa en su permanencia, como antes le interesaba solamente en su desaparición; pues su subsistencia se convierte para ella en su propia verdad y en su propia presencia; la conciencia tiene ahora la certeza de experimentarse solamente en él."""
    },
    {
        "id": "r03",
        "pagina": 144,
        "texto": """La razón es la certeza de la conciencia de ser toda realidad; de este modo expresa el idealismo el concepto de la razón. Del mismo modo que la conciencia que surge como razón abriga de un modo inmediato en sí esta certeza, así también el idealismo la expresa de un modo inmediato: yo soy yo, en el sentido de que el yo que es mi objeto, es objeto con la conciencia del no ser de cualquier otro objeto, es objeto único, es toda realidad y toda presencia, y no como en la autoconciencia en general, ni tampoco como en la autoconciencia libre, ya que allí sólo es un objeto vacío en general y aquí solamente un objeto que se repliega de los otros que siguen rigiendo junto a él. Pero la autoconciencia sólo es toda realidad no solamente para sí, sino también en sí al devenir esta realidad o más bien al demostrarse como tal. Y se demuestra así en el camino por el que, primero en el movimiento dialéctico de la supresión, la percepción y el entendimiento, el ser otro desaparece como en sí, y luego en el movimiento que pasa por la independencia de la conciencia en el señorío y la servidumbre, por el pensamiento de la libertad, la liberación escéptica y la lucha de la liberación absoluta de la conciencia desdoblada dentro de sí, el ser otro en cuanto sólo es para ella, desaparece para ella misma. Aparecerían sucesivamente dos lados, uno en que la esencia o lo verdadero [tenía] para la conciencia la determinabilidad del ser, [y] otro [en que] su determinabilidad era el ser solamente para ella. Pero ambos lados se reducían a una verdad, la de que lo que es o el en sí sólo es en cuanto es para la conciencia y lo que es para ella es también en sí. La conciencia que es esta verdad ha dejado atrás y olvidado este camino al surgir de un modo inmediato como razón; dicho en otros términos, esta razón que surge de un modo inmediato surge solamente como la certeza de aquella verdad. De este modo, sólo asevera ser toda realidad, pero sin concebirla ella misma, pues aquel camino olvidado es el concebir esta afirmación expresada de un modo inmediato. Y, asimismo, para quien no lo ha recorrido, resulta también inconcebible esta afirmación, cuando la escucha bajo esta forma pura, ya que, expresada bajo una figura concreta él mismo llega muy bien a ella."""
    },
    {
        "id": "r04",
        "pagina": 145,
        "texto": """El idealismo que, en vez de presentar dicho camino, comienza por esta afirmación, es también, por tanto, una pura aseveración, que ni se concibe a sí misma ni puede hacerse concebible a otros. El idealismo expresa una certeza inmediata a la que se contraponen otras certezas inmediatas, sólo que se han perdido por aquel camino. Así, pues, junto a la aseveración de aquella certeza aparecen, con el mismo derecho, las aseveraciones de estas otras certezas. La razón invoca la autoconciencia de cada conciencia: yo soy yo, mi objeto y esencia es yo, y ninguna de aquellas conciencias negará esta verdad ante aquél. Pero, al fundamentarla sobre esta invocación, la razón sanciona la verdad de la otra certeza, a saber, la de que hay otro para mí, la de que un otro que yo es para mí objeto y esencia o de que en cuanto soy yo mi objeto y mi esencia sólo lo soy al replegarme de lo otro en general y ponerme junto a ello como una realidad. Sólo cuando la razón aparece como reflexión desde esta certeza contrapuesta aparece su afirmación de sí, no sólo como certeza y aseveración, sino como verdad, y no solamente junto a otras verdades, sino como la verdad única. La aparición inmediata es la abstracción de su ser presente, cuya esencia y ser en sí son el concepto absoluto, es decir, el movimiento de su ser devenido. La conciencia determinará de diferente modo su actitud ante el ser otro o ante su objeto según el grado en que se halle del espíritu del mundo que va cobrando conciencia de sí. El modo como en cada caso encuentra y determina de un modo inmediato a sí mismo y a su objeto o cómo sea para si dependerá de lo que haya devenido o de lo que ya en sí sea."""
    },
    {
        "id": "r05",
        "pagina": 145,
        "texto": """La razón es la certeza de ser toda realidad. Pero este en sí o esta realidad es todavía algo completamente universal, la pura abstracción de la realidad. Es la primera positividad que la autoconciencia es en sí misma, para sí y yo, por tanto, solamente la pura esencialidad de lo que es o la categoría simple. La categoría, que tenía fuera de este caso la significación de ser la esencialidad de lo que es, la esencialidad indeterminada de lo que es en general o de lo que es frente a la conciencia, pasa a ser ahora esencialidad o unidad simple de lo que es solamente como realidad pensante; o bien significa que autoconciencia y ser son la misma esencia; la misma, no en la comparación, sino en y para sí. Solamente el mal idealismo unilateral hace que esta unidad reaparezca como conciencia en uno de los lados y frente a ella un en sí. Ahora bien, esta categoría o la unidad simple de la autoconciencia y el ser lleva en sí la diferencia, pues su esencia está precisamente en ser de un modo inmediato igual a sí misma en el ser otro o en la diferencia absoluta. La diferencia es, por tanto, pero de un modo totalmente transparente y como una diferencia que, al mismo tiempo, no lo es. Se manifiesta como una multiplicidad de categorías. En cuanto el idealismo enuncia la unidad simple de la autoconciencia como toda realidad y hace de ella de un modo inmediato la esencia, sin haberla concebido como esencia absolutamente negativa —solamente ésta lleva en sí misma la negación, la determinabilidad o la diferencia—, es todavía más inconcebible que esto, el que haya en la categoría diferencias o especies."""
    },
    {
        "id": "r06",
        "pagina": 146,
        "texto": """Esta aseveración en general, así como la aseveración de un número determinado de especies de la categoría es una nueva aseveración, pero que implica en ella misma el que no deba aceptarse ya simplemente como tal. En efecto, en cuanto que la diferencia comienza en el yo puro, en el entendimiento puro mismo, ello lleva implícito el que aquí se abandonan la inmediatez, el asegurar y el encontrar, y comienza el concebir. Ahora bien, el tomar la multiplicidad de las categorías, del modo que sea, como algo que se encuentra, partiendo por ejemplo de los juicios, y aceptarlas así, constituye, en realidad, como una afrenta a la ciencia: ¿dónde podría el entendimiento poner de manifiesto una necesidad, si no pudiera hacerlo en él mismo, que es la necesidad pura?

Ahora bien, si la pura esencialidad de las cosas, lo mismo que su diferencia, pertenece así a la razón, parece que, en rigor, no debiera poder hablarse de cosas, es decir, de algo que sólo sería para la conciencia lo negativo de sí misma. En efecto, las muchas categorías son especies de la categoría pura, lo que significa que ésta sigue siendo su género o su esencia, pero no algo contrapuesto a aquellas. Pero dichas categorías son ya lo ambiguo, que, en su multiplicidad, lleva en sí, al mismo tiempo, el ser otro frente a la categoría pura. En realidad, entran en contradicción con ella a través de esta multiplicidad, y la unidad pura no tiene más remedio que superar en sí esta multiplicidad, constituyéndose como unidad negativa de las diferencias. Pero, como unidad negativa, excluye de sí tanto las diferencias en cuanto tales como aquella primera unidad pura inmediata como tal, y es singularidad; una nueva categoría, que es conciencia excluyente, es decir, que es de tal modo que un otro es para ella. La singularidad es su paso de su concepto a una realidad externa, el puro esquema que es conciencia y que, con ello, por ser singularidad y uno excluyente, es también la referencia a un otro. Pero este otro de esta categoría son solamente las otras primeras categorías, a saber: esencialidad pura y diferencia pura; y en ella, es decir, precisamente en el ponerse el otro o en este otro mismo, es la conciencia ella misma. Cada uno de estos momentos distintos remite a otro, pero sin que por esto se llegue en ellos, al mismo tiempo, a un ser otro. La categoría pura remite a las especies, que pasan a la categoría negativa o a la singularidad; y ésta remite, a su vez, de rechazo, a aqué-"""
    },
    {
        "id": "r07",
        "pagina": 148,
        "texto": """razón de un otro que se nos había presentado ya como el suponer, el percibir y como el entendimiento que aprehendía lo supuesto y lo percibido. Semejante saber es afirmado al mismo tiempo como un saber no verdadero por el concepto de este idealismo mismo, ya que sólo la unidad de la apercepción es la verdad del saber. La razón pura de este idealismo, para llegar a este otro que le es esencial, es decir, que es, por tanto, el en sí, pero que no lo tiene en ella misma, es remitida de nuevo, por medio de ella misma, a aquel saber que no es un saber de lo verdadero; de este modo, se condena, a sabiendas y por su voluntad, a un saber no verdadero y no puede apartarse del suponer y el percibir, que no encierran verdad alguna para ella misma. Se halla en contradicción inmediata, al afirmar como la esencia algo doble y sencillamente contrapuesto, la unidad de la apercepción y, al mismo tiempo, la cosa que, aunque se la llame el impulso ajeno, la esencia empírica, o la sensibilidad o la cosa en sí, sigue permaneciendo la misma en su concepto extraña a dicha unidad.

Este idealismo ha caído en esta contradicción porque afirma el concepto abstracto de la razón como lo verdadero; por eso mismo nace de un modo inmediato para él la realidad como algo que no es la realidad de la razón, mientras que la razón debiera ser, al mismo tiempo, toda realidad; permanece como una búsqueda sin descanso, que en la búsqueda misma explica como algo sencillamente imposible la satisfacción del encontrar. No es tan inconsecuente, sin embargo, la razón real, sino que, siendo primeramente tan sólo la certeza de ser toda realidad, es consciente en este concepto de la certeza de no ser todavía, como certeza, como yo, la realidad en verdad y se ve empujada a elevar su certeza a verdad y a llenar el mío vacío.

A. RAZÓN OBSERVANTE

Esta conciencia, para la que el ser tiene la significación de lo suyo, la vemos ahora entrar nuevamente en la suposición y la percepción, pero no como en la certeza de lo que es solamente otro, sino con la certeza de ser este otro mismo. Anteriormente, sólo le había acaecido percibir y experimentar algo en la cosa, pero, al llegar aquí, ella misma dispone las observaciones y la experiencia. El suponer y el percibir, que antes se habían superado para nosotros, son ahora superados para la conciencia misma; la razón aspira a saber la verdad, a encontrar como concepto lo que para la suposición y la percepción es una cosa, es decir, a tener en la sociedad solamente la conciencia de sí misma."""
    },
    {
        "id": "r08",
        "pagina": 148,
        "texto": """La razón tiene ahora, por tanto, un interés universal en el mundo, precisamente porque tiene la certeza de estar presente en él o de que lo presente es racional. Busca su otro, sabiendo que en él no posee sino a sí misma, busca su infinitud en él, pero sólo encuentra cosas, y sólo las encuentra; y es un instinto, pues sólo así encuentra su propia determinación en el objeto y se satisface en él. En tanto que el instinto de la razón no tiene aún en sí mismo otro que su objeto, en el sentido de que no ha llegado aún a la ciencia, el instinto se ve impulsado por el objeto mismo y, por el contrario, a través de la razón, al hallarse el objeto de la conciencia contrapuesto a la conciencia, el objeto es absorbido y cancelado. La conciencia, tal como se presenta inmediatamente como razón, tiene la certeza de aquella relación, pero, en cuanto se contrapone al objeto como un ser otro, su certeza no es aún verdad; es la certeza de que ella misma es toda realidad, pero de que este objeto no es todavía para ella esta certeza."""
    },
    {
        "id": "r09",
        "pagina": 149,
        "texto": """La conciencia es, pues, el instinto de la razón que, sin tener a ésta, se ve empujado hacia lo otro, y precisamente porque no tiene aún este otro —su infinitud—, y el movimiento del instinto cancela el ser otro y se da en el objeto la intuición de sí mismo. Este instinto de la razón es el observar. Por tanto, su sentir ya no es un sentir inmediato, sino un sentir instintivo que eleva el objeto a la forma del concepto y, por medio del objeto, se convierte en sí mismo en concepto y, al mismo tiempo, lo es para sí mismo. La observación, en este su movimiento, comienza por la conciencia sensible, que es para ella lo más bajo, pero que, al mismo tiempo, es para ella su esencia, la cual, sin embargo, es todavía para ella otra cosa. La conciencia sensible es aquí, por tanto, para ella, lo verdadero, pero no de un modo inmediato, sino como un ser otro que ella misma, y que ella, sin embargo, tiene que asumir y convertir en sí misma."""
    },
    {
        "id": "r10",
        "pagina": 149,
        "texto": """a. LA OBSERVACIÓN DE LA NATURALEZA

Cuando la conciencia observante va más allá de esta conciencia sensible y llega al pensamiento, al concepto, éste es para ella una esencia que, al mismo tiempo, no es su esencia; es un concepto que está en las cosas y que ella simplemente encuentra. En esta primera forma del instinto de la razón, la conciencia no se busca a sí misma en lo que observa, sino que busca su otro; y está segura de encontrar en él su esencia, pero en la figura de una cosa. De ahí que para ella el concepto aparezca como un concepto natural, como un concepto que es, que ella encuentra, pero no sabe que este concepto es ella misma. La observación tiene, por tanto, ante sí, en primer lugar, el ser como ser, es decir, lo encuentra en la forma de la inmediatez, y sus determinaciones se le ofrecen como determinaciones quietas, persistentes, que ella se limita a recibir. El movimiento del ser y su proceso se le ofrecen también, pero como algo que ya ha sido hecho y que ella se limita a recibir."""
    },
    {
        "id": "r11",
        "pagina": 150,
        "texto": """La observación, como instinto de la razón, busca lo universal; pero lo universal que ella encuentra es, primeramente, la especie, el género. La especie es lo universal que ha surgido de la comparación de los individuos y que, al mismo tiempo, es algo que es, que se halla presente en ellos. Pero la razón no se satisface con este universal, porque éste no es el concepto mismo, sino un universal abstracto que se ha obtenido por la eliminación de las diferencias. El instinto de la razón quiere encontrar la necesidad en la relación de estas diferencias, quiere encontrar la ley. Pero la ley es, en primer lugar, una relación universal y permanente, que se manifiesta en el cambio de los fenómenos. La conciencia observante se esfuerza por encontrar leyes, por ejemplo, la ley de la caída de los cuerpos, la ley de la refracción de la luz, etc. Estas leyes son, ciertamente, universales, pero no son todavía el concepto; son relaciones entre determinabilidades que se manifiestan como independientes y subsistentes por sí mismas. La ley es la imagen estable del fenómeno inestable; pero esta imagen no es todavía el concepto, que es la unidad de los opuestos."""
    },
    {
        "id": "r12",
        "pagina": 151,
        "texto": """El instinto de la razón llega, en la observación, hasta el concepto de la ley, pero este concepto no es para ella mismo. Para ella, la ley es algo que es; encuentra la ley, pero no sabe que ella misma es la que la ha puesto. La razón no se reconoce en la ley; la ley es para ella un ser otro, un algo extraño. La razón tiene que experimentar que ella misma es la esencia de la ley, que la ley no es algo extraño, sino su propia esencia. Pero esta experiencia sólo se hará cuando la razón, en su movimiento, llegue a ser para sí misma lo que la ley es en sí. Por ahora, la ley es para ella solamente un objeto, y ella se comporta hacia él como observación."""
    },
    {
        "id": "r13",
        "pagina": 152,
        "texto": """En la medida en que la razón observante encuentra leyes, éstas son para ella leyes de la naturaleza; no son todavía leyes del espíritu. Las leyes de la naturaleza son relaciones entre determinabilidades que se manifiestan como cosas independientes; por ejemplo, la relación entre el peso específico y la cohesión, entre la sensibilidad y la irritabilidad en lo orgánico, etc. La razón observante trata de encontrar tales relaciones, y cree que en ellas ha encontrado su esencia. Pero la esencia de la razón no es esta relación de cosas independientes, sino la unidad que supera esta independencia. La razón sólo se encontrará a sí misma cuando el objeto de su observación sea ella misma, es decir, cuando observe el espíritu."""
    },
    {
        "id": "r14",
        "pagina": 153,
        "texto": """b. LA OBSERVACIÓN DE LO ORGÁNICO

El instinto de la razón se vuelve ahora hacia lo orgánico. Lo orgánico es un objeto en el que la razón puede esperar encontrarse a sí misma, porque lo orgánico es, en sí mismo, un concepto real, es decir, es un individuo que se mantiene a sí mismo en su relación con otro. Lo orgánico es un fin en sí mismo; su ser es su actividad, y su actividad es mantenerse a sí mismo. En lo orgánico, la razón encuentra, por tanto, la unidad del concepto y de la realidad, que es la esencia de la razón misma. Pero, al principio, lo orgánico es para la razón observante un objeto, un ser otro, y ella se comporta hacia él como observación. La razón busca en lo orgánico leyes, por ejemplo, la ley de la relación entre la sensibilidad y la irritabilidad, o la ley de la relación entre lo interno y lo externo en el organismo."""
    },
    {
        "id": "r15",
        "pagina": 154,
        "texto": """Lo orgánico se ofrece a la observación bajo una doble forma: como una totalidad de propiedades simples y universales, y como una totalidad de partes reales, de la figura. Las propiedades simples son, por ejemplo, la sensibilidad, la irritabilidad y la reproducción. Estas propiedades no son cosas independientes, sino momentos fluidos del concepto orgánico. La figura, por el contrario, es el ser quieto, la existencia de lo orgánico en el espacio. La observación trata de relacionar estos dos lados, de encontrar leyes que expresen cómo la figura es la expresión de aquellas propiedades simples. Pero esta relación es difícil de aprehender, porque las propiedades simples no tienen una existencia separada en la figura, sino que penetran todas las partes de la figura y son, cada una de ellas, el todo mismo."""
    },
    {
        "id": "r16",
        "pagina": 155,
        "texto": """La observación intenta fijar los momentos del concepto orgánico como sistemas particulares de la figura: la sensibilidad como sistema nervioso, la irritabilidad como sistema muscular, la reproducción como sistema de órganos internos. Pero estos sistemas no son, en realidad, más que abstracciones de la anatomía; en el organismo vivo, estos momentos no están separados, sino que son procesos que recorren todo el organismo. La sensibilidad está en los músculos tanto como en los nervios; la irritabilidad está en los nervios tanto como en los músculos. Por tanto, la pretensión de encontrar leyes entre estos sistemas es vana; no hay una correspondencia fija entre un momento del concepto y una parte de la figura."""
    },
    {
        "id": "r17",
        "pagina": 156,
        "texto": """La observación, al no poder encontrar leyes en la relación entre los momentos del concepto y las partes de la figura, se vuelve hacia la relación entre lo orgánico y lo inorgánico. Intenta establecer leyes como: los animales que viven en el aire tienen la estructura de las aves, los que viven en el agua tienen la estructura de los peces, etc. Pero estas leyes son superficiales y están llenas de excepciones. Lo orgánico tiene la libertad de sustraerse a estas determinaciones; no hay una necesidad interna en la relación entre el medio y la forma orgánica. El concepto de pez no lleva implícito el concepto de agua, ni el de ave el de aire. Por tanto, estas relaciones no merecen el nombre de leyes."""
    },
    {
        "id": "r18",
        "pagina": 157,
        "texto": """Lo que la observación no logra captar en estas relaciones externas es el concepto de fin que constituye la esencia de lo orgánico. Lo orgánico es fin en sí mismo; se mantiene a sí mismo en su relación con otro. La necesidad que rige en lo orgánico es una necesidad interna, no una relación externa entre elementos independientes. Pero esta necesidad interna no es visible para la observación; la observación sólo ve relaciones externas y contingentes. El concepto de fin permanece oculto para ella, porque la observación se mueve en el elemento del ser y no en el del concepto."""
    },
    {
        "id": "r19",
        "pagina": 158,
        "texto": """La observación intenta, sin embargo, aprehender este concepto de fin de una manera objetiva. Lo orgánico se muestra a la observación como algo que se conserva a sí mismo; su acción no produce otra cosa que a sí mismo. Pero la observación no reconoce en esto el concepto, porque establece una diferencia entre el fin y el ser para sí, entre la acción y el resultado. Esta diferencia no es para ella una diferencia, pero la conciencia no ve la unidad. La acción orgánica le parece una acción contingente, cuyo fin no está en ella misma. Y así, lo orgánico, que en sí es concepto, se convierte para la observación en una cosa incomprensible."""
    },
    {
        "id": "r20",
        "pagina": 159,
        "texto": """La autoconciencia se halla constituida del mismo modo que lo orgánico: se distingue de sí de tal modo que, al mismo tiempo, no resulta de ello diferencia alguna. En la observación de la naturaleza orgánica, la autoconciencia no encuentra, por consiguiente, nada más que esta esencia, se encuentra como una cosa, como una vida, pero estableciendo, además, una diferencia entre lo que ella misma es y lo que ha encontrado, lo que no es diferencia alguna. Así como el instinto animal busca y consume el alimento, pero sin que con ello produzca otra cosa que a sí mismo, así también el instinto de la razón se encuentra solamente a sí mismo en su búsqueda. El animal termina por el sentimiento de sí. En cambio, el instinto de la razón es, al mismo tiempo, autoconciencia; pero, por ser solamente instinto, es dejado a un lado frente a la conciencia y tiene en ella su oposición."""
    },
    {
        "id": "r21",
        "pagina": 160,
        "texto": """La determinación de lo orgánico como fin en sí mismo lleva implícito que la necesidad se presenta bajo la forma de una relación contingente. La libertad de lo orgánico consiste en comportarse hacia su ser necesario como algo indiferente; el concepto de la cosa cae fuera de su ser. La razón tiene, asimismo, la necesidad de contemplar su propio concepto como algo que cae fuera de ella y, por tanto, como una cosa tal que, frente a ella, la razón es indiferente, y que por su parte es indiferente frente a la razón y a su propio concepto. Como instinto, la razón permanece también dentro de este ser o de la indiferencia, y la cosa que expresa el concepto sigue siendo para ella algo distinto de este concepto y el concepto algo distinto de la cosa. Por donde la cosa orgánica sólo es para la razón fin en ella misma en el sentido de que la necesidad que se presenta como oculta en su acción cae fuera de lo orgánico mismo."""
    },
    {
        "id": "r22",
        "pagina": 161,
        "texto": """La unidad de la universalidad y la actividad no es para la conciencia observante, ya que dicha unidad es esencialmente el movimiento interior de lo orgánico y sólo puede aprehenderse como concepto; y la observación busca los momentos solamente en la forma del ser y la permanencia. Puesto que la totalidad orgánica consiste esencialmente en no tener en ella ni permitir encontrar en ella los momentos, la conciencia transforma desde su punto de vista la oposición en una oposición que es conforme a él. La esencia orgánica nace así para la conciencia como una relación de dos momentos fijos y que son, oposición cuyos dos lados, por tanto, parece que, de una parte, le son dados en la observación, mientras que de otra parte expresan de acuerdo con su contenido la oposición entre el concepto orgánico del fin y la realidad, pero de una manera oscura y superficial, en la que el pensamiento desciende al plano de la representación."""
    },
    {
        "id": "r23",
        "pagina": 162,
        "texto": """La conciencia observante sugiere que lo externo es solamente expresión de lo interno. Estas mismas determinaciones de la relación, a saber: la independencia indiferente de lo distinto, y en ella su unidad, dentro de la que aquellas desaparecen, las hemos visto en el concepto de fin. Debemos ver ahora qué figura adoptan en su ser lo interno y lo externo. Lo interno como tal debe tener un ser externo y una figura, ni más ni menos que lo externo como tal, pues es un objeto o, dicho de otro modo, ello mismo se pone como lo que es y se halla presente para la observación. La sustancia orgánica, como sustancia interna, es el alma simple, el puro concepto de fin o lo universal, que al dividirse permanece asimismo como fluidez universal y, por tanto, se manifiesta en su ser como la acción o el movimiento de la realidad que tiende a desaparecer, mientras que lo externo, contrapuesto a lo interno que es, subsiste en el ser quieto de lo orgánico."""
    },
    {
        "id": "r24",
        "pagina": 163,
        "texto": """La ley, como la relación entre aquel interno y este externo, expresa así su contenido, de una parte, en la presentación de momentos universales o esencialidades simples y, de otra parte, en la presentación de la esencialidad realizada o de la figura. Aquellas primeras propiedades orgánicas simples, para llamarlas así, son la sensibilidad, la irritabilidad y la reproducción. Estas propiedades, por lo menos las dos primeras, no parecen relacionarse, es verdad, con el organismo en general, sino con el organismo animal solamente. En realidad, el organismo vegetal sólo expresa el concepto simple del organismo, que no desarrolla sus momentos, razón por la cual, al referirnos a ellos, tal y como deben ser para la observación, debemos atenernos a aquel organismo que presenta su existencia desarrollada. Por lo que a los momentos mismos se refiere, éstos se dependen de un modo inmediato del concepto de autofinalidad. En efecto, la sensibilidad expresa en general el concepto simple de la reflexión orgánica en sí o la fluidez universal de dicho concepto; la irritabilidad, por su parte, expresa la elasticidad orgánica, que le permite comportarse en la reflexión, al mismo tiempo, como algo que reacciona, y es la realización contrapuesta al primer ser en sí quieto, en que aquel ser para sí abstracto es un ser para otro. Por último, la reproducción es la acción de este organismo total reflejado en sí, su actividad como cosa en sí o como todo."""
    },
    {
        "id": "r25",
        "pagina": 164,
        "texto": """Si se distinguen estos momentos, como es necesario, se los distinguirá de acuerdo con el concepto, y su oposición será cualitativa. Pero, si además de esta diferencia verdadera, se los pone como distintos, en cuanto que son y para la representación, como pueden ser los lados de una ley, se manifestarán en diversidad cuantitativa. Su peculiar oposición cualitativa aparece entonces en la magnitud y surgirán leyes tales como, por ejemplo, la de que la sensibilidad y la irritabilidad se hallan en razón inversa a su magnitud, de tal modo que al aumentar la una disminuye la otra; o, mejor dicho, tomando la magnitud misma como contenido, la de que la magnitud de algo aumenta a medida que disminuye su pequeñez. Pero si a esta ley se le da un contenido determinado, diciendo por ejemplo que la magnitud de un agujero aumenta a medida que disminuye lo que lo llena, tenemos que esta razón inversa puede convertirse igualmente en una razón directa y expresarse así, diciendo que la magnitud del agujero aumenta en razón directa a lo que se saca de él; proposición tautológica, ya se exprese como razón directa o inversa, y que en su peculiar expresión sólo querrá decir que una magnitud aumenta cuando aumenta esta magnitud."""
    },
    {
        "id": "r26",
        "pagina": 165,
        "texto": """Así como el agujero y lo que lo llena y se retira de él son cosas cualitativamente contrapuestas, pero lo real de ellas y su determinada magnitud es uno y lo mismo en ambos casos y como el aumento de la magnitud y la disminución de la pequeñez es lo mismo y su contraposición carente de sentido se reduce a una tautología, los momentos orgánicos son igualmente inseparables en su realidad y en su magnitud, que es la magnitud de aquélla; la una sólo aumenta con la otra y disminuye con ella, ya que lo uno sólo tiene sentido en cuanto se halla presente lo otro; o más bien es indiferente considerar un fenómeno orgánico como irritabilidad o como sensibilidad, en general y lo mismo cuando se habla de su magnitud. Del mismo modo, es indiferente que el aumento de un agujero se exprese como ampliación del agujero mismo o de lo que lo llena y se extrae de él. O bien un número, por ejemplo tres, tiene la misma magnitud, lo mismo se lo tome positiva o negativamente, y si lo aumento de tres a cuatro, se convertirá en cuatro así lo positivo como lo negativo, del mismo modo que el polo Sur de la brújula tiene exactamente la misma fuerza que el polo Norte o que una electricidad positiva o un ácido representan la misma fuerza que su electricidad negativa o que la base sobre la que el ácido actúa."""
    },
    {
        "id": "r27",
        "pagina": 166,
        "texto": """Es claro que en este modo de formular leyes las cosas ocurren, propiamente, de tal modo que la irritabilidad y la sensibilidad comienzan constituyendo la contraposición orgánica determinada; pero este contenido se pierde y la oposición se desvía por el formal aumento y disminución de la magnitud o de la diferente intensidad y extensión, una oposición que ya no afecta para nada a la naturaleza de la sensibilidad y la irritabilidad y que ha dejado de expresarla. De ahí que este juego vacuo de la formulación de leyes no se halle vinculado a los momentos orgánicos, sino que puede aplicarse a todo, y descansa, en general, en la ignorancia de la naturaleza lógica de estas contraposiciones. Por último, si, en vez de la sensibilidad y la irritabilidad, relacionamos con la una o con la otra la reproducción, vemos que no se da ni siquiera ocasión para esta formulación de leyes, pues la reproducción no está en una contraposición con aquellos momentos como cada uno de éstos con el otro, y como quiera que esta formulación de leyes se basa en dicha contraposición, aquí desaparece incluso la apariencia de ella."""
    },
    {
        "id": "r28",
        "pagina": 167,
        "texto": """Este modo de formular leyes que se acaba de considerar implica las diferencias del organismo en el sentido de momentos de su concepto, por lo cual debería ser, propiamente, una formulación de leyes apriorística. Pero, además, lleva consigo esencialmente el pensamiento de que tales diferencias tienen el significado de diferencias dadas y, por lo demás, la conciencia meramente observante tiene que atreverse solamente a su ser allí. La realidad orgánica lleva necesariamente implícita esa contraposición, que su concepto expresa y que puede determinarse como irritabilidad y sensibilidad, del mismo modo que ambos conceptos se manifiestan, a su vez, como distintos de la reproducción. La exterioridad en que aquí se consideran los momentos del concepto orgánico es la peculiar e inmediata exterioridad de lo interno, no lo externo, que es externo en su conjunto y que es figura, y en relación con lo cual puede luego considerarse lo interno. Pero, aprehendida así la oposición entre los momentos, tal y como es en el ser allí, sensibilidad, irritabilidad y reproducción descienden a propiedades comunes, que, en relación las unas con las otras, son universalidades tan indiferentes entre sí como el peso específico, el color, la dureza, etc."""
    },
    {
        "id": "r29",
        "pagina": 168,
        "texto": """En este sentido, puede observarse, evidentemente, que un organismo es más sensible, más irritable o encierra una capacidad mayor de reproducción que otro o que la sensibilidad etc. de uno difiere de la de otro según la especie, que uno se comporta ante determinados incentivos de un modo más sensible o más irritable que otro, como el caballo, por ejemplo, se comporta de otro modo ante la cebada que ante el heno o el perro, a su vez, adopta distinto comportamiento ante ambos, etc., de la misma manera que puede observarse que un cuerpo es más duro que otro, etc. Sin embargo, estas propiedades sensibles, la dureza, el color, etc., así como los fenómenos de la excitabilidad ante la cebada, de la irritabilidad ante la carga o de la disposición para dar a luz una cantidad o una calidad de crías, referidas las unas a las otras y comparadas entre sí, contradicen esencialmente a una conformidad a ley. En efecto, la determinabilidad de su ser sensible consiste precisamente en que existen de un modo completamente indiferente las unas con respecto a las otras y presentan la libertad de la naturaleza sustraída al concepto más bien que la unidad de una relación, más bien su oscilación irracional en la escala de la magnitud contingente entre los momentos del concepto que estos momentos mismos."""
    },
    {
        "id": "r30",
        "pagina": 169,
        "texto": """El otro lado, según el cual los momentos simples del concepto orgánico son comparados con los momentos de la configuración, sería el que podría dar la ley propiamente dicha, que enunciaría lo externo verdadero como la huella de lo interno. Ahora bien, como aquellos momentos simples son propiedades fluidas y que se compenetran, no tienen en la cosa orgánica una expresión real y desglosada, como lo que se llama un sistema singular de la figura. O bien, si la idea abstracta del organismo sólo se expresa verdaderamente en aquellos tres momentos porque no son nada estables, sino solamente momentos del concepto y del movimiento, entonces, por el contrario, el organismo como configuración no se capta en dichos tres sistemas determinados, tal como la anatomía los disocia. En la medida en que tales sistemas deben ser encontrados en su realidad y legítimos por el hecho de encontrarlos, debe tenerse presente también que la anatomía no muestra solamente los tres sistemas en cuestión, sino muchos más. Y así, aun prescindiendo de esto, el sistema sensible en general tiene que significar algo completamente distinto que lo que se llama sistema nervioso, el sistema irritable algo distinto que el sistema muscular, o el sistema reproductivo algo distinto que los órganos de la reproducción. En los sistemas de la figura como tal se aprehende al organismo con arreglo al lado abstracto de la existencia muerta; sus momentos, así captados, pertenecen a la anatomía y al cadáver, no al conocimiento y al organismo vivo. En estas partes, aquellos momentos han dejado ya más bien de ser, pues han dejado de ser procesos."""
    },
    {
        "id": "r31",
        "pagina": 170,
        "texto": """Puesto que el ser del organismo es esencialmente universalidad o reflexión en sí mismo, el ser de su totalidad, como el de sus momentos, no puede subsistir en un sistema anatómico, sino que la expresión real y su exterioridad se dan más bien solamente como un movimiento que discurre a través de las distintas partes de la configuración y en el que lo que se desgaja y se fija como sistema singular se presenta esencialmente como un momento fluido, de tal modo que no es aquella realidad como la anatomía la encuentra la que puede valer como su realidad, sino sólo como proceso, fuera del cual no tendrían tampoco un sentido las partes anatómicas. De aquí se desprende, pues, que los momentos de lo interno orgánico, tomados de por sí, no pueden suministrar los lados de una ley del ser, ya que en una ley tal se predican de un ser allí, difieren uno de otro y no podría enunciarse el uno en vez del otro; y asimismo que, al ponerse en uno de los lados, no tendrían en el otro su realización en un sistema fijo, pues este sistema ni contiene, en general, una verdad orgánica ni es tampoco la expresión de aquellos momentos de lo interno. Lo esencial de lo orgánico, puesto que es en sí lo universal, es más bien, en general, el tener sus momentos en la realidad de un modo igualmente universal, es decir, como procesos que se desarrollan en todo, pero no en ofrecer una imagen de lo universal en una cosa aislada."""
    },
    {
        "id": "r32",
        "pagina": 171,
        "texto": """De este modo, en lo orgánico se pierde, en general, la representación de una ley. La ley trata de aprehender y expresar la oposición como entre lados quietos y, en ellos, la determinabilidad, que es su relación mutua. Lo interno, a lo que pertenece la universalidad fenoménica, y lo externo, a lo que pertenecen las partes de la figura quieta, deberían constituir los lados correspondientes entre sí de la ley, pero, mantenidos así separados, pierden su significación orgánica; y la representación de la ley se basa precisamente en que sus dos lados tengan una subsistencia indiferente que es para sí y en que la relación se distribuya entre ellos como una doble determinabilidad, en correspondencia mutua. Pero, cada lado de lo orgánico es más bien en él mismo una universalidad simple, en la que se disuelven todas las determinaciones, y es el movimiento de esta disolución. Penetrando en la diferencia entre este modo de formular leyes y las formas anteriores, se esclarecerá plenamente su naturaleza. En efecto, si nos fijamos retrospectivamente en el movimiento de la percepción y del entendimiento que en ella se refleja en sí mismo y determina con ello su objeto, vemos que este entendimiento, aquí, no tiene ante sí, en su objeto, la relación entre estas determinaciones abstractas, entre lo universal y lo singular, entre lo esencial y lo externo, sino que es él mismo el tránsito para el que este tránsito es objeto; y es así como aquí, en lo orgánico, el tránsito se ha convertido en objeto mismo."""
    },
    {
        "id": "r33",
        "pagina": 172,
        "texto": """c. LA OBSERVACIÓN DE LA AUTOCONCIENCIA

La observación de la naturaleza no ha dado a la razón lo que ésta buscaba: no ha encontrado en ella su propia esencia, el concepto. La razón se vuelve ahora hacia sí misma, hacia la autoconciencia, y busca observarse a sí misma. Pero la autoconciencia no es un objeto que pueda ser observado del mismo modo que un objeto natural. La autoconciencia es esencialmente movimiento, proceso, y no un ser quieto. La observación, que se atiene al ser, no puede captar este movimiento. Por tanto, la observación de la autoconciencia tiene que adoptar una forma diferente: tiene que observar las manifestaciones de la autoconciencia, sus expresiones externas, sus productos. La autoconciencia se manifiesta en el lenguaje, en la acción, en las obras. La observación trata de encontrar en estas manifestaciones leyes que expresen la relación entre lo interno (la intención, el pensamiento) y lo externo (la palabra, la acción, la obra)."""
    },
    {
        "id": "r34",
        "pagina": 173,
        "texto": """La primera forma de esta observación es la de las leyes del pensamiento, la lógica. La lógica presenta las leyes del pensamiento puro, las formas universales del concepto. Pero estas leyes son formas vacías; no tienen realidad. Son, ciertamente, la verdad formal, pero no la verdad plena. La lógica no es la ciencia de la realidad, sino solamente la ciencia de la forma del pensamiento. Por tanto, la razón no puede satisfacerse con la lógica; necesita un contenido. La observación de la autoconciencia busca, entonces, en la psicología las leyes de la vida anímica. La psicología observa las facultades y las actividades del alma: la sensibilidad, la inteligencia, la voluntad. Pero también aquí encuentra la razón leyes que no son más que generalizaciones empíricas, sin necesidad interna. La psicología describe, pero no explica; no alcanza el concepto."""
    },
    {
        "id": "r35",
        "pagina": 174,
        "texto": """La observación de la autoconciencia llega así a la fisiognómica y a la frenología, que pretenden leer en lo externo (la expresión del rostro, la forma del cráneo) lo interno (el carácter, las disposiciones del alma). Estas pseudociencias son el extremo de la observación, el punto donde la razón, al no poder encontrarse en lo interno ni en lo externo por separado, intenta encontrar la relación entre ambos en algo sensible. Pero esta relación es, en realidad, una relación invertida: se pretende que el espíritu sea un hueso, que la forma del cráneo sea la expresión del carácter. La frenología es la culminación de la observación de la autoconciencia, y también su autodisolución. En ella, la razón se encuentra a sí misma de la manera más extraña: se encuentra como una cosa, como un hueso. Esta es la ironía suprema de la observación: la razón que buscaba encontrarse en el mundo se encuentra, al final, como un objeto muerto."""
    },
    {
        "id": "r36",
        "pagina": 175,
        "texto": """La observación de la autoconciencia ha recorrido, pues, el camino desde las leyes lógicas, pasando por las leyes psicológicas, hasta la fisiognómica y la frenología. En cada una de estas etapas, la razón ha buscado su esencia en un objeto, y en cada una ha fracasado, porque la esencia de la razón no es un objeto, sino el movimiento mismo de ponerse y superarse. La observación de la autoconciencia termina, por tanto, con la constatación de que la razón no puede encontrarse a sí misma en el mundo de los objetos, sino que debe buscarse en otra parte. Este es el paso a la razón práctica, a la razón que actúa y transforma el mundo."""
    },
    {
        "id": "r37",
        "pagina": 176,
        "texto": """Lo que la observación no logra es comprender que lo interno y lo externo son la misma cosa, pero que esta identidad no es una identidad quieta, sino una identidad que se realiza en el movimiento. El espíritu no es una cosa que tenga un interior y un exterior; el espíritu es el movimiento mismo de exteriorizarse y retornar a sí. La observación, al fijar lo interno como una cosa y lo externo como otra, no puede captar este movimiento. Por eso la frenología es el punto culminante y también el punto de quiebre de la observación: en ella, la razón se ve a sí misma de la manera más absurda, como un hueso, y esto la obliga a renunciar a la observación y a buscar otro camino."""
    },
    {
        "id": "r38",
        "pagina": 177,
        "texto": """La crítica de la frenología es, por tanto, la conclusión de la razón observante. La razón ha aprendido que no puede encontrarse a sí misma en el mundo de los objetos, sino que debe producirse a sí misma en el mundo. La razón que observa es todavía una razón pasiva, que se limita a recibir el mundo. La razón que actúa, en cambio, es una razón activa, que transforma el mundo y se realiza en él. Este es el paso a la siguiente sección: la realización de la autoconciencia racional."""
    },
    {
        "id": "r39",
        "pagina": 178,
        "texto": """En la frenología, la relación entre lo interno y lo externo se invierte de la manera más grotesca. Lo interno, el espíritu, debe ser conocido por lo externo, el cráneo. Pero el cráneo es un hueso, un objeto muerto, y pretender que el espíritu sea un hueso es el colmo del absurdo. Sin embargo, este absurdo tiene su razón de ser: es la consecuencia última de la observación que busca el concepto en el ser. La observación lleva necesariamente a este resultado, porque no puede captar la unidad viviente del concepto y lo real. Al fijar los momentos por separado, termina por identificarlos de la manera más burda: el concepto es una cosa, el espíritu es un hueso. Esta es la ironía de la observación, y también su autodisolución."""
    },
    {
        "id": "r40",
        "pagina": 179,
        "texto": """Con la crítica de la frenología, la razón observante ha llegado a su fin. La razón ha aprendido que no puede encontrarse a sí misma en el mundo de los objetos, porque ella misma es el principio de ese mundo. La razón no es una cosa entre las cosas; es la actividad que pone y supera las cosas. Por tanto, la razón debe dejar de observar y comenzar a actuar. Debe dejar de buscar su esencia en el mundo y debe empezar a producir su esencia en el mundo. Este es el paso a la razón práctica, a la razón que realiza su libertad en el mundo."""
    },
    {
        "id": "r41",
        "pagina": 180,
        "texto": """b. LA OBSERVACIÓN DE LA AUTOCONCIENCIA EN SU PUREZA Y EN SUS RELACIONES CON LA REALIDAD EXTERNA; LEYES LOGICAS Y LEYES PSICOLÓGICAS

La observación de la naturaleza encuentra el concepto realizado en la naturaleza inorgánica, encuentra leyes cuyos momentos son cosas, que se comportan al mismo tiempo como abstracciones; pero este concepto no es una simplicidad reflejada dentro de sí. En cambio, la vida de la naturaleza orgánica sólo es esta simplicidad reflejada dentro de sí; la contraposición de sí misma, como la contraposición entre lo universal y lo singular, no se desdobla en la esencia de esta vida misma; la esencia no es el género que se escinde y se mueve en sus momentos indiferenciados y que en su contraposición es, a la par, indiferenciado para sí mismo. La observación encuentra este concepto libre, cuya universalidad tiene en ella misma de un modo no menos absoluto la singularidad desarrollada, solamente en el concepto mismo existente como concepto o en la autoconciencia.

[1. Las leyes del pensamiento]

Al volverse sobre sí misma y dirigirse hacia el concepto real como concepto libre, la observación descubre primeramente las leyes del pensamiento. Esta singularidad que el pensamiento es en él mismo es el movimiento abstracto de lo negativo, totalmente replegado sobre la simplicidad, y las leyes se hallan fuera de la realidad. No tienen realidad [Realität] alguna, lo que significa, en general, sencillamente que carecen de verdad. No deben ser, ciertamente, la verdad entera, pero sí, por lo menos, la verdad formal. Sin embargo, lo puramente formal sin realidad [Realität] es la cosa discursiva o la abstracción vacía sin llevar en ella la escisión que no sería sino el contenido. Pero, de otra parte, en cuanto son leyes del pensamiento puro y éste lo universal en sí y, por tanto, un saber que lleva en sí de un modo inmediato el ser y en él toda realidad [Realität], estas leyes son conceptos absolutos e indiferenciados, las esencialidades tanto de la forma como de las cosas. Como la universalidad que se mueve en sí es el concepto simple escindido, tiene de este modo contenido en sí, y un contenido que es el contenido todo, pero no es un ser sensible. Es un contenido que no se halla en contradicción..."""
    },
    {
        "id": "r42",
        "pagina": 181,
        "texto": """...con la forma ni en general separado de ella, sino que es más bien, esencialmente, ella misma; pues esta forma no es otra cosa que lo general que se separa en sus momentos puros.

Ahora bien, del modo como esta forma o este contenido es para la observación como observación, adquiere la determinación de un contenido encontrado, dado, es decir, de un contenido que solamente es. Deviene un ser quieto de relaciones, una multitud de necesidades delimitadas que debe tener verdad como un contenido fijo en y para sí, en su determinabilidad, lo que de hecho lo sustrae a la forma. Pero esta verdad absoluta de determinabilidades fijas o de muchas leyes distintas contradice a la unidad de la autoconciencia o del pensamiento y la forma, en general. Lo que se enuncia como ley fija y permanente en sí sólo puede ser un momento de la unidad que se refleja en sí misma, sólo puede aparecer como una magnitud llamada a desaparecer. Pero, arrancadas por la consideración a esta cohesión del movimiento y formuladas como algo singular, no carecen de contenido, pues tienen un contenido determinado, sino que carecen más bien de la forma, que es su esencia. En efecto, estas leyes no son la verdad del pensamiento, no precisamente porque sean puramente formales y carezcan de contenido, sino más bien por la razón opuesta, porque, en su determinabilidad o cabalmente como un contenido al que se ha sustraído la forma, tienen que valer como algo absoluto. En su verdad, como momentos llamados a desaparecer en la unidad del pensamiento, debieran ser tomadas como saber o movimiento pensante, pero no como leyes del saber. Ahora bien, la observación no es el saber mismo ni lo conoce, sino que invierte su naturaleza en la figura del ser, es decir, concibe su negatividad solamente como leyes del ser. Aquí, es suficiente con haber puesto del manifiesto la no validez de las llamadas leyes del pensamiento partiendo de la naturaleza universal de la cosa. El desarrollo esto más a fondo corresponde a la filosofía especulativa, donde dichas leyes se revelarán como lo que en verdad son, a saber: como momentos singulares llamados a desaparecer y cuya verdad es solamente la totalidad del movimiento pensante, el saber mismo."""
    },
    {
        "id": "r43",
        "pagina": 181,
        "texto": """[2. Leyes psicológicas]

Esta unidad negativa del pensamiento es para sí misma o, mejor dicho, es el ser para sí mismo, el principio de la individualidad y, en su realidad [Realität], conciencia operante. Hacia ella, como hacia la realidad [Realität] de aquellas leyes, se ve llevada, por tanto, la conciencia observadora por la naturaleza de la cosa. En cuanto que esta conexión no es para la conciencia observadora, ésta opina que el pensamiento queda ante ella a un lado y que del otro obtiene otro ser en lo que ahora es para ella el objeto, a saber, la conciencia operante, la cual es para sí de tal modo que supera el ser otro y tiene su realidad en esta intuición de sí misma como de lo negativo.

Se abre aquí, por tanto, para la observación un nuevo campo en la realidad actuante de la conciencia. La psicología contiene la multitud de leyes con arreglo a las cuales se comporta de manera distinta ante los diversos modos de su realidad como ante un ser otro encontrado; se trata, en parte, de recibir en sí estos diversos modos y de conformarse a los hábitos, costumbres y al modo de pensar encontrados como aquello en que el espíritu se es objeto como realidad y, en parte, de saberse como actuando por su cuenta ante todo eso con la mira de extraer para sí, siguiendo su inclinación y su pasión, solamente lo particular y conformándose a lo objetivo; en el primer caso, el espíritu adopta un comportamiento negativo ante sí mismo en cuanto singularidad, en el segundo, se comporta negativamente hacia sí como ser universal. Según el primer lado, la independencia se limita a dar a lo encontrado la forma de la individualidad consciente en general, permaneciendo en lo tocante al contenido dentro de la realidad universal encontrada; según el segundo, en cambio, introduce en ésta, por lo menos, una peculiar modificación, que no contradice a su contenido esencial, o bien otra modificación mediante la que el individuo se contrapone a ella como realidad particular y contenido peculiar y que adopta la forma de una transgresión criminal cuando el individuo supera dicha realidad de un modo simplemente singular o cuando lo hace de un modo universal y con ello para todos, suplantando por otros el mundo, el derecho, la ley y las costumbres existentes."""
    },
    {
        "id": "r44",
        "pagina": 182,
        "texto": """La psicología basada en la observación, que enuncia primeramente sus percepciones de los modos universales que se le presentan en la conciencia activa, se encuentra con diversas facultades, inclinaciones y pasiones y, como el recuerdo de la unidad de la autoconciencia no puede descartarse en la enumeración de aquella colección de facultades, etc., la psicología basada en la observación tiene necesariamente que llegar, por lo menos, hasta asombrarse de que en el espíritu puedan juntarse como en un saco tantas cosas diversas contingentes y heterogéneas entre sí, tanto más cuanto que no se muestran, allí, como cosas inertes y muertas, sino como movimientos llenos de inquietud.

En la enumeración de estas diferentes facultades, la observación se atiene al lado universal; la unidad de estas múltiples capacidades es el lado contrapuesto a esta universalidad, es la individualidad real. A su vez, el aprehender y enumerar las individualidades reales diferenciadas de tal modo que un hombre se incline más a esto y el otro a aquello, que el uno tenga más entendimiento que el otro, lleva en sí, sin embargo, algo mucho menos interesante que incluso la enumeración de las especies de insectos, de musgos, etc.; pues éstas dan derecho a la observación a tomarlas así, como algo singular y carente de concepto, ya que forman parte del elemento de la individualidad contingente. Por el contrario, el tomar la individualidad consciente carente de espíritu como una manifestación singular que es, entraña lo contradictorio de que su esencia es lo universal del espíritu. Sin embargo, como la aprehensión hace entrar a la individualidad, al mismo tiempo, en la forma de la universalidad, encuentra su ley; parece ahora tener un fin racional y cumplir una función necesaria."""
    },
    {
        "id": "r45",
        "pagina": 183,
        "texto": """[3. La ley de la individualidad]

Los momentos que constituyen el contenido de la ley son, de una parte, la individualidad misma y, de otra, su naturaleza inorgánica universal, a saber, las circunstancias, la situación, los hábitos, las costumbres, la religión, etc., encontrados; partiendo de estos elementos hay que concebir la individualidad determinada. Dichos elementos contienen algo determinado y algo universal y son, al mismo tiempo, algo presente que se ofrece a la observación y se expresa de otro lado bajo la forma de la individualidad.

La ley de esta relación entre ambos lados debiera contener ahora el tipo de efecto e influencia que estas determinadas circunstancias ejercen sobre la individualidad. Pero esta individualidad consiste precisamente en ser también lo universal y, por tanto, en confluir de un modo quieto e inmediato con lo universal presente, con los hábitos y costumbres, etc., y conformarse a ellos, lo mismo que el comportarse como algo contrapuesto ante ellos y el invertirlos más bien, así como el comportarse de un modo totalmente indiferente frente a ellos en su singularidad, el no dejarlos influir sobre sí y el no mostrarse activo en contra de ellos. Lo que influya sobre la individualidad y cuál influencia deba ejercer —lo que, propiamente, significa lo mismo— dependerá, por tanto, solamente de la individualidad misma; decir que esta individualidad llega a ser así esta individualidad determinada vale tanto como decir que ya lo ha sido. Circunstancias, situaciones, hábitos, etc. que, de una parte, se muestran como presentes y que, de otra parte, lo están en esta determinada individualidad, expresan solamente la esencia determinada de la misma individualidad, de la que no hay por qué ocuparse. De no mediar estas circunstancias, este modo de pensar, estos hábitos, este estado del mundo en general, no cabe duda de que el individuo no habría llegado a ser lo que es, ya que esta sustancia universal es todo lo que se encuentra en este lado del mundo. Pero, tal y como se particulariza en este individuo —que es el que se trata de concebir—, es necesario que el estado del mundo se particularice en y para sí y que actúe sobre un individuo en esta determinabilidad que se ha dado; solamente así habrá hecho de este individuo determinado lo que él es. Si lo externo se estructurase en y para sí tal y como se manifiesta en la individualidad, ésta se concebiría partiendo de aquello. Tendríamos, entonces, una doble galería de imágenes, una de las cuales sería el reflejo de la otra: una, la galería de la total determinabilidad y delimitación de las circunstancias externas y otra, que sería la misma, traducida al modo en que son en la esencia consciente; la primera, la superficie de la esfera y la segunda el centro que ella representa en sí."""
    },
    {
        "id": "r46",
        "pagina": 184,
        "texto": """Pero esta superficie esférica, el mundo del individuo, tiene de un modo inmediato la doble significación de ser mundo y situación que son en y para sí y el mundo del individuo, o bien en cuanto éste se limitaría a confluir con él, haciéndolo entrar dentro de sí tal y como es, comportándose frente a él solamente como conciencia formal, o bien sería el mundo del individuo en cuanto que lo presente fuera invertido por él. Como, en virtud de esta libertad, la realidad es susceptible de esta doble significación, el mundo del individuo sólo puede concebirse partiendo de este mismo; y la influencia de la realidad, que se representa como lo que es en y para sí, sobre el individuo cobra a través de éste el sentido absolutamente contrapuesto de que o deja que el curso de la realidad que afluye siga su marcha sin intervenir en él o lo interrumpe e invierte. Pero, de este modo, la necesidad psicológica se trueca en una palabra tan vacua, que se da la posibilidad absoluta de que lo que deba haber experimentado esta influencia no haya sido influido para nada.

Desaparece con ello el ser que sería en y para sí y que debería constituir uno de los lados de una ley, y cabalmente su lado universal. La individualidad es lo que es su mundo, en cuanto suyo; ella misma es el círculo de su acción, en el que se ha presentado como realidad y es, simple y únicamente, la unidad del ser dado y del ser construido; unidad cuyos lados no se desdoblan, como en la representación de la ley psicológica, en el mundo en sí presente y en la individualidad que es para sí; o bien, si cada uno de estos lados es considerado..."""
    },
    {
        "id": "r47",
        "pagina": 186,
        "texto": """su acción. En la consideración psicológica, había que relacionar entre sí la realidad que es en y para sí y la individualidad determinada; aquí, en cambio, es objeto de observación la individualidad total determinada; y cada uno de los lados de su oposición es, a su vez, este todo. Por tanto, al todo externo pertenece no sólo el ser originario, el cuerpo congénito, sino también la formación de este mismo, que pertenece a la actividad de lo interior; el cuerpo es la unidad del ser no formado y del ser formado y la realidad del individuo penetrada por el ser para sí. Este todo, que abarca en sí las determinadas partes fijas originarias y los rasgos que sólo brotan a través de la acción, es, y este ser es expresión del interior, del individuo puesto como conciencia y como movimiento. Y este interior no es ya tampoco la propia actividad formal, carente de contenido o indeterminada, cuyo contenido y cuya determinabilidad residieran, como antes, en las circunstancias externas, sino que es un carácter originario y determinado en sí, cuya forma es solamente la actividad. Por consiguiente, lo que aquí hay que considerar es la relación entre estos dos lados, para ver cómo puede determinarse y qué debe entenderse por esta expresión de lo interior en lo exterior.

[1. La significación fisonómica de los órganos]

Este lado externo, primeramente, sólo como órgano hace visible lo interior o, en general, hace de ello un ser para otro; pues lo interior, en cuanto es en el órgano, es la actividad misma. La boca que habla, la mano que trabaja y, si se quiere, también las piernas, son los órganos realizadores y ejecutores, que tienen en ellos la acción como acción o lo interior como tal; pero la exterioridad que lo interior cobra por medio de ellos es el hecho, como una realidad ya desglosada del individuo. Lenguaje y trabajo son exteriorizaciones en las que el individuo no se retiene y posee ya en él mismo, sino en que deja que lo interior caiga totalmente fuera de sí y lo abandona a algo otro. Por eso podemos decir tanto que estas exteriorizaciones expresan demasiado lo interior como que lo expresan demasiado poco; demasiado, porque lo interior mismo irrumpe en ellas, porque no permanece oposición alguna entre éste y aquéllas; no sólo expresan lo interior, sino que lo expresan de modo inmediato; demasiado poco, porque lo interior, al pasar al lenguaje y a la acción, se convierte en otro y se entrega así a merced del elemento de la transformación..."""
    },
    {
        "id": "r48",
        "pagina": 187,
        "texto": """...que invierte la palabra hablada y el hecho consumado, haciendo de ellos algo distinto de lo que en sí y para sí son, como actos de este determinado individuo. Las obras de los actos, no sólo pierden, al exteriorizarse, por las influencias de otros, el carácter de ser algo permanente con respecto a otras individualidades, sino que, además, al comportarse como un exterior particularizado e indiferente con respecto a lo interior, pueden ser, como interior y a través del individuo mismo, algo otro de como se manifiestan, bien porque deliberadamente lo conviertan en la manifestación de algo otro de lo que en verdad son, bien porque el individuo no acierte a exteriorizarse como propiamente quiere hacerlo y a afianzar su exteriorización de tal modo que otros no puedan deformar su obra. Por tanto, la acción, como obra consumada, tiene la doble significación contrapuesta de ser o bien la individualidad interior y no su expresión, o bien, como lo exterior, una realidad libre del interior y que es algo completamente distinta de esto. Por esta ambigüedad, debemos volver la vista hacia el interior tal y como aún es en el individuo mismo, pero de un modo visible y exterior. Pero, en el órgano, lo interior sólo es como la acción inmediata misma que cobra su exterioridad en el hecho, el cual puede o no representar lo interior. Por tanto, el órgano, considerado con arreglo a esta oposición, no garantiza la expresión buscada."""
    },
    {
        "id": "r49",
        "pagina": 187,
        "texto": """Ahora bien, si la sola figura exterior, en cuanto no es órgano o acción, es decir, como un todo quieto, pudiera expresar la individualidad interior, se comportaría como una cosa subsistente que recibiría estrictamente lo interior como algo extraño en su ser allí pasivo, convirtiéndose así en el signo de ello —una expresión exterior contingente, cuyo lado real carecería para sí de significación—, un lenguaje cuyos sonidos y combinaciones de sonidos no serían la cosa misma, sino algo enlazado con ella caprichosamente y puramente contingente para ella.

Semejante conexión arbitraria de momentos que son algo exterior los unos con respecto a los otros no suministra ley alguna. La fisiognómica pretende distinguirse de otras falsas ciencias y de otros estudios malsanos en cuanto que considera la individualidad determinada en la necesaria oposición de algo interior y algo exterior, del carácter como esencia consciente y del carácter como figura que es, relacionando entre sí estos dos momentos tal como aparecen entrelazados por su concepto y como, por tanto, deben constituir el contenido de una ley. Por el contrario, en la astrología, la quironancia y en otras ciencias semejantes, parece que lo exterior sólo es referido a lo exterior, que algo sólo es referido a algo extraño a ello. Tal o cual constelación coincidente con el día del nacimiento y, acercando más al cuerpo mismo este algo exterior, tales o cuales rasgos de la mano, son momentos exteriores en cuanto a la mayor o menor duración de la vida y al destino del hombre individual en general. En cuanto exterioridades, estos momentos mantienen un comportamiento indiferente entre sí y no tienen los unos con respecto a los otras la necesidad que debe contenerse en la relación entre lo exterior y lo interior."""
    },
    {
        "id": "r50",
        "pagina": 188,
        "texto": """Es cierto que la mano no parece ser algo hasta tal punto exterior para el destino, sino comportarse con respecto a éste más bien como algo interior. En efecto, el destino es también, a su vez, solamente la manifestación de lo que es la individualidad determinada en sí como determinabilidad originaria interior. Ahora bien, para saber lo que esta determinabilidad es en sí, el quironmante y el fisonomista recurren a un método más corto que Solón, por ejemplo, quien consideraba que eso sólo podía llegar a saberse ateniéndose al curso de toda la vida; Solón consideraba la manifestación, mientras que aquéllos consideran el en sí. Y que la mano debe representar el en sí de la individualidad con respecto a su destino se ve fácilmente considerando que la mano es, después del órgano del lenguaje, el que más permite al hombre manifestarse y realizarse. Es el artífice animado de su dicha; de ella puede decirse que es lo que el hombre hace, pues en la mano como en el órgano activo de la realización de sí mismo se halla presente el hombre como animador, y en cuanto que el hombre es originariamente su propio destino, la mano expresará, por tanto, este en sí.

De la determinación según la cual el órgano de la actividad es en él tanto un ser como la acción o de que en él está presente el ser en sí interior mismo y tiene un ser para otros, se desprende otra apreciación acerca del órgano, distinta de la anterior. En efecto, si se mostrara que los órganos en general no pueden tomarse como expresiones de lo interior porque en ellos se halla presente la acción como acción y, en cambio, la acción como hecho es algo puramente exterior, y lo interior y lo exterior se bifurcan de este modo y ambos momentos son o pueden ser extraños el uno al otro, el órgano debería tomarse, a su vez, con arreglo a la determinación considerada, como el término medio entre ambos, en cuanto que precisamente esto, el que la acción sea presente en él, constituye al mismo tiempo una exterioridad de la acción, diferente, además, de lo que es el hecho, puesto que aquélla pertenece al individuo y permanece en él. Este término medio y unidad de lo interior y lo exterior es también ello mismo, ahora, exterior; pero al mismo tiempo, esta exterioridad es acogida en lo interior; se enfrenta, como simple exterioridad, a la exterioridad dispersa que, o bien no es más que una obra o un estado singular, contingente para la individualidad toda, o bien, como exterioridad total, es el destino escindido en multitud de obras y estados. Por tanto, los rasgos simples de la mano, así como el tono y el volumen de la voz como determinabilidad individual del lenguaje —y también éste en cuanto adquiere por medio de la mano una existencia más fija que por medio de la voz, el lenguaje escrito, concretamente en su modalidad de escritura autógrafa—, todo esto es expresión de lo interior, de tal modo que, como exterioridad simple, vuelve a enfrentarse a la múltiple exterioridad del obrar y del destino, se comporta como algo interior con respecto a esto. Así, pues, si primeramente se toma como lo interior, como la esencia del obrar y del destino, la naturaleza determinada y la peculiaridad congénita del individuo, unidas a lo que éste ha llegado a ser por medio de la cultura, el individuo tiene primeramente su manifestación y su exterioridad en su boca, en su mano, en su voz, en su escritura autógrafa así como en los demás órganos y en sus permanentes determinabilidades; y sólo después se expresa más ampliamente al exterior en su realidad en el mundo."""
    },
    {
        "id": "r51",
        "pagina": 189,
        "texto": """Como ahora este término medio se determina como la exteriorización que al mismo tiempo se ha retrotraído al interior, su existencia no se limita al órgano inmediato de la acción, sino que es más bien el movimiento y la forma del rostro y de la configuración en general, que nada llevan a cabo. Estos rasgos y su movimiento son, con arreglo a este concepto, la acción retenida, que permanece en el individuo y, en su relación con la acción real, el propio vigilante y observante de aquél, la exteriorización como reflexión sobre la exteriorización real. El individuo, de este modo, no queda mudo en su acción exterior y con respecto a ella, porque al mismo tiempo se refleja en sí y exterioriza este ser reflejado en sí; y esta acción teórica o el lenguaje del individuo consigo mismo acerca de esto es también perceptible para otros, porque es él mismo una exteriorización.

[2. La multivocidad de esta significación]

En este interior, que en su exteriorización permanece interior, es observado el ser reflejado del individuo desde su realidad; y hay que ver qué ocurre con esta necesidad puesta en esta unidad. Ante todo, este ser reflejado es distinto del hecho mismo y puede, por tanto, ser algo otro y ser tomado por algo otro de lo que es; mirando a la cara de una persona, vemos si toma en serio lo que dice o hace. Pero, a la inversa, lo que debe ser expresión de lo interior es, al mismo tiempo, una expresión que es, con lo que recae a su vez en la determinación del ser, el cual es absolutamente contingente para la esencia consciente de sí misma. Es, por ello, evidentemente, expresión, pero es también, al mismo tiempo, simplemente un signo, lo que hace que la constitución de aquello por lo que se expresa sea totalmente indiferente para el contenido expresado. Lo interior, en esta manifestación, es sin duda un invisible visible, pero sin hallarse vinculado a ella; lo mismo podría darse en otra manifestación, como en la misma manifestación otro interior. De ahí que Lichtenberg diga con razón: Suponiendo que el fisonomista haya logrado atrapar al hombre una sola vez, bastaría con una valerosa decisión para hacerse de nuevo incomprensible por miles de años. Así como en la relación anterior las circunstancias concurrentes eran un algo que es, del que la individualidad tomaba lo que ella podía y quería, bien sometiéndose a ellas, bien invirtiéndolas, razón por la cual ese ser no contenía la necesidad ni la esencia de la individualidad, así también aquí es el ser inmediato de la individualidad que se manifiesta un ser que o bien expresa su ser reflejado desde la realidad y su ser en sí o bien sólo es para ella un signo indiferente con respecto a lo designado y que, por tanto, no designa nada en verdad; ese signo es tanto el rostro de la individualidad como la máscara de que se puede despojar. La individualidad impregna su figura, se mueve y habla en ella; pero toda esa existencia se presenta también como un ser indiferente con respecto a la voluntad y a la acción; la individualidad cancela en él la significación que antes tenía, la de tener en él su ser reflejado en sí o su verdadera esencia y pone ahora esto, por el contrario, en la voluntad y en el hecho."""
    },
    {
        "id": "r52",
        "pagina": 190,
        "texto": """La individualidad abandona aquel ser reflejado en sí que se expresa en los rasgos y pone su esencia en la obra. En ello, la individualidad contradice al comportamiento establecido por el instinto de la razón, el cual se basa en la observación de la individualidad consciente de sí con vistas a fijar su interior y su exterior. Este punto de vista nos lleva al pensamiento que en rigor sirve de base a la ciencia —si así queremos llamarla— fisonómica. La oposición con la que da esta observación es, en cuanto a la forma, la oposición entre lo práctico y lo teórico —pero ambos lados puestos dentro de lo práctico mismo—, la oposición entre la individualidad que se realiza en el obrar, tomando éste en el sentido más general, y la que, emanando al mismo tiempo de este obrar, se refleja en sí y el obrar es su objeto. La observación acoge esta oposición en la misma relación invertida que la determina en la manifestación. Considera como lo exterior no esencial el hecho mismo y la obra, la del lenguaje o la de una realidad más sólida, y como lo interior esencial el ser en sí de la individualidad. De los dos lados que la conciencia práctica tiene en sí, la intención y el hecho —la suposición con respecto a su modo de obrar y el obrar mismo—, la observación elige el primero como el interior verdadero; el segundo, según ella, es su exteriorización más o menos inesencial en el hecho, pues su exteriorización verdadera la tiene en su figura. Esta última exteriorización es la presencia sensible inmediata del espíritu individual; la interioridad que debe ser la verdadera es la peculiaridad de la intención y la singularidad del ser para sí; ambas constituyen el espíritu supuesto. Por tanto, lo que la observación tiene como objetos es la existencia supuesta, y es aquí donde la observación indaga leyes.

La suposición inmediata acerca de la presencia supuesta del espíritu es la fisiognómica natural, el juicio precipitado sobre la naturaleza interior y el carácter de su figura, a primera vista. El objeto de esta suposición es de tal modo, que lleva en su esencia el ser en verdad algo distinto de su ser sensible inmediato. Lo presente, la visibilidad como visibilidad de lo invisible, lo que es objeto de observación es, sin duda, cabalmente este ser reflejado en sí en lo sensible y partiendo de ello. Pero, precisamente esta presencia inmediata sensible es la realidad del espíritu, tal y como ésta es sólo para la superación; y la observación gira en torno a este lado, con su existencia supuesta, con la fisonomía, la escritura autógrafa, el timbre de la voz, etc. Relaciona esa existencia cabalmente con este interior supuesto. No se trata de reconocer al asesino o al ladrón, sino la calidad de serlo; la determinabilidad abstracta firme se pierde, así, en la determinabilidad infinita concreta del individuo singular, la cual reclama ahora descripciones harto más ingeniosas que aquellas calificaciones. Evidentemente, estas descripciones más ingeniosas dicen más de lo que podrían decir calificaciones como asesino, ladrón, bondadoso, íntegro, etc., pero no bastan, ni mucho menos, para el fin que se persigue, que es el enunciar el ser supuesto o la individualidad singular, como no bastan las descripciones de la figura que van más allá de la frente achatada, la nariz larga, etc. Pues la figura singular, como la autoconciencia singular, es, en cuanto ser supuesto, inexpresable. La ciencia del conocimiento del hombre que recae sobre el supuesto hombre, lo mismo que la fisiognómica que tiende hacia su supuesta realidad y pretende elevar a un saber los juicios carentes de conciencia de la fisiognómica natural, es, por tanto, algo interminable y sin base, que jamás puede llegar a decir lo que supone, porque es limitada a suponerlo y su contenido es solamente algo supuesto."""
    },
    {
        "id": "r53",
        "pagina": 191,
        "texto": """Las leyes que esta ciencia trata de descubrir son relaciones entre estos dos lados supuestos y, por tanto, ellas mismas no pueden ser otra cosa que una suposición vacía. Por el hecho también de que este supuesto saber, que pretende ocuparse de la realidad del espíritu, tiene como su objeto precisamente el que se refleje en sí saliendo desde su existencia sensible y de que la existencia determinada sea para él una contingencia indiferente, tiene necesariamente que saber de un modo inmediato que las leyes por él descubiertas no dicen nada, sino que son pura charlatanería o se limitan a dar una suposición de sí; expresión cuya verdad se limita a enunciar como uno y lo mismo esto: a decir su suposición, con lo cual no se aporta la cosa misma, sino solamente una suposición de sí. Ahora bien, en cuanto al contenido, tales observaciones en nada difieren de estas otras: 'Siempre que hay feria, llueve', dice el tendero; 'y también siempre que tiendo la ropa a secar', dice el ama de casa.

Lichtenberg, quien caracteriza así la observación fisiónómica, escribe además: 'Si alguien dijera que obras como un hombre honrado, pero que yo veo por tu figura que te constriñes y que en el fondo de tu corazón eres un granuja, no cabe duda de que a estas palabras cualquier persona decente replicaría hasta el fin del mundo con una bofetada'. Semejante réplica es certera, porque equivale a la refutación de lo que constituye el primer supuesto de la tal ciencia de la suposición, a saber, que la realidad del hombre es su rostro, etc. El verdadero ser del hombre es, por el contrario, su obrar; en éste es la individualidad real y él es el que supera lo supuesto en sus dos lados. De una parte, lo supuesto, como un ser corporal estático; la individualidad se presenta más bien en el obrar como la esencia negativa, que sólo es en tanto supera el ser. De otra parte, el obrar supera asimismo la inexpresabilidad de la suposición en lo tocante a la individualidad consciente de sí, que es en la suposición una individualidad infinitamente determinada y determinable. En el obrar consumado, se aniquila esta falsa infinitud. El hecho es algo simplemente determinado, universal, que puede captarse en una abstracción; es un asesinato, un robo o una acción benéfica o heroica, etc., y puede decirse de él lo que es, y su ser no es solamente un signo, sino la cosa misma. Es esto, y el hombre individual es lo que dicho acto es; en la simplicidad de este ser, el hombre individual es para otros una esencia universal que es, y deja de ser una esencia solamente supuesta. Cierto que no se pone en esto como espíritu; pero, en cuanto que se habla de su ser como ser y, de una parte, se contrapone el doble ser, el de la figura y el del obrar, debiendo ser su realidad tanto la una como el otro; hay que afirmar, más bien, como su auténtico ser solamente el obrar, no su figura, que debiera expresar simplemente lo que el individuo supone de sus actos o lo que se supone que podría hacer."""
    },
    {
        "id": "r54",
        "pagina": 192,
        "texto": """Y como, de otra parte, su obra y su posibilidad interior, su capacidad o intención son también contrapuestas, solamente aquélla, la obra, puede considerarse como su verdadera realidad, aunque él mismo se engañe acerca de ello y, retornando de su obrar a sí mismo, suponga ser en este interior otro que en el obrar. La individualidad que se confía al elemento objetivo, al convertirse en obra, se abandona indudablemente a él y se presta a verse cambiada e invertida. Pero el carácter del obrar lo determina precisamente el que sea un ser real el que se mantiene o solamente una obra supuesta, que desaparece en sí, anulándose. La objetividad no hace cambiar el hecho mismo, sino que se limita a poner de manifiesto lo que éste es, es decir, si es o no es nada. La desmembración de este ser en intenciones y sutilezas por el estilo mediante las cuales se trata de explicar de nuevo al hombre real, es decir, sus actos, retrotrayéndolo a un ser supuesto, cualesquiera que puedan ser sus intenciones particulares con respecto a su propia realidad, deben abandonarse a la ociosidad de la suposición, la cual, si quiere llevar a cabo su inoperante sabiduría, negar a quien obra el carácter de la razón y maltratarlo de este modo, explicando como el ser la figura y los rasgos, en vez de los actos, debe encontrarse con la réplica indicada más arriba, la que le mostrará que la figura no es el en sí, sino que puede ser, más bien, un objeto de tratamiento."""
    },
    {
        "id": "r55",
        "pagina": 192,
        "texto": """[3. La frenología]

Si nos fijamos ahora en general en el conjunto de las relaciones en las que puede observarse la individualidad autoconsciente con respecto a su lado exterior, vemos que queda atrás una que la observación debe tomar todavía como objeto. En la psicología es la realidad exterior de las cosas la que debe tener en el espíritu su continuum consciente de ella y hacer así al espíritu concebible. Por el contrario, en la fisiognómica el espíritu debe darse a conocer en su propio exterior como un ser que es el lenguaje —la visible invisibilidad de su esencia. Resta aún la determinación del lado de la realidad en que la individualidad expresa su esencia en su realidad inmediata, fija, puramente existente. Esta última relación se distingue, por tanto, de la relación fisionómica por el hecho de que ésta es la presencia hablada del individuo, que en su exterior..."""
    },
    {
        "id": "r56",
        "pagina": 193,
        "texto": """razón —que no es tan mala, en este caso— para circunscribir este ser allí al cráneo. Y si a alguno se le ocurriese pensar en la espalda por cuanto que también, a veces, el saber y la acción se reciben y transmiten a través de ella, esto nada probaría, por probar demasiado, en apoyo de que la médula espinal deba considerarse como sede del espíritu y la columna vertebral como contraimagen de su ser allí; esto nada probaría, porque probaría demasiado, pues cabe asimismo recordar que también son predilectas otras vías exteriores para alcanzar la actividad del espíritu, para estimularla o retenerla. Podemos, pues, si queremos, prescindir con entera razón, de la columna vertebral; y cabe también construir una doctrina de filosofía natural tan buena como muchas otras sosteniendo que el cráneo por sí solo no contiene los órganos del espíritu. En efecto, esto ha sido anteriormente eliminado del concepto de esta relación, tomando por ello el cráneo como lado del ser allí y, si no se debiera recordar el concepto de la cosa, la experiencia se encarga de enseñar que si se ve con el ojo como órgano, no se mata ni se roba, se hace poesía, etc. con el cráneo. Por tanto, debemos abstenernos de emplear la expresión órgano para designar aquella significación del cráneo de la que aún hemos de tratar. Pues aunque se suele decir que lo que importa en el hombre razonable no es la palabra, sino la cosa, ello no quiere decir que sea lícito designar una cosa con una palabra que no le corresponde; esto es una torpeza y, al mismo tiempo, un fraude: se supone y se pretexta no disponer de la palabra adecuada, ocultando que lo que falta es, de hecho, la cosa, es decir, el concepto; si éste se hallara presente, dispondría también de su palabra adecuada. Por el momento, hemos determinado solamente esto: que así como el cerebro es la cabeza viva, el cráneo es el caput mortuum."""
    },
    {
        "id": "r57",
        "pagina": 193,
        "texto": """[β] Relación entre la forma del cráneo y la individualidad

Así, pues, en este ser muerto tendrían que darse los movimientos espirituales y los modos determinados del cerebro su representación de realidad externa, realizada que, sin embargo, es todavía en el individuo mismo. En cuanto a la relación entre estos movimientos espirituales y el cráneo, que, como ser muerto, no tiene el espíritu inmanente en sí mismo, se ofrece primeramente la relación establecida más arriba, la relación mecánica exterior, de tal modo que los órganos propiamente dichos —que son en el cerebro— expresan unas veces el cráneo en forma redonda y otras veces lo ensanchan o lo achatan o influyen sobre él de cualquier otro modo que uno se quiera representar. Siendo él mismo una parte del organismo, hay que pensar, sin embargo, que en el cráneo, como en un hueso vivo, debe concebirse una correlación viva con el cerebro, de tal modo que aquél se amolde a éste y reciba en sí la impresión de su configuración, como la cabeza, en general, amolda su órbita al ojo. Pero al mismo tiempo, la acción recíproca de esta relación viva se halla disuelta por el hecho de que este lado del ser del cerebro y del cráneo, tomado en esta unidad viva, es igualmente una exterioridad, en la cual el ser para otro recae sobre el ser. El cráneo, por tanto, puede ser considerado, ciertamente, como un producto del cerebro que exterioriza al interior como signo, no de su actividad, sino de su ser. Pero, al mismo tiempo, en esta unidad viva, la misma relación recíproca suprime la independencia de ambos lados el uno con respecto al otro y la contingencia de la influencia; el cerebro conserva la libertad para no ejercer influencia sobre el cráneo o, si la ejerce, para que no aparezca como un obrar, sino como un proceso vivo inconsciente e indiferente, por el cual el cerebro y el cráneo pueden estar juntos en la relación como toda causa y efecto, pero su vinculación permanece para ellos un secreto, ya que ésta no se hace visible en su ser allí. En ella, la influencia del uno sobre el otro es solamente un suponer para sí, un juicio subjetivo, que puede estar tan acertado como equivocado, acerca de una conexión que no se manifiesta. Por tanto, en todo esto no se gana nada para la determinación de lo interior por lo exterior."""
    },
    {
        "id": "r58",
        "pagina": 194,
        "texto": """La observación, que trata de encontrar la relación entre el cerebro y el cráneo, parte del supuesto de que el cerebro es lo interior y el cráneo lo exterior. Pero este supuesto es falso, porque el cráneo no es la expresión del cerebro, sino simplemente un hueso. Si se pretendiera que la forma del cráneo expresa las cualidades espirituales del individuo, se estaría afirmando que el espíritu es un hueso, lo cual es un absurdo. Sin embargo, esta afirmación absurda es la consecuencia necesaria de la observación que busca lo interior en lo exterior. La frenología es, por tanto, el punto culminante de la observación de la autoconciencia, y también su autodisolución. En ella, la razón se encuentra a sí misma de la manera más extraña: se encuentra como una cosa, como un hueso. Esta es la ironía suprema de la observación: la razón que buscaba encontrarse en el mundo se encuentra, al final, como un objeto muerto.

La frenología pretende establecer leyes como: tal protuberancia en el cráneo indica tal facultad espiritual. Pero estas leyes son puramente arbitrarias; no hay ninguna necesidad en la relación entre la forma del cráneo y el carácter. Además, el cráneo es un hueso, algo muerto, mientras que el espíritu es vida y movimiento. Pretender que lo muerto exprese lo vivo es el colmo del extravío. La frenología es, pues, una pseudociencia que no merece siquiera el nombre de ciencia."""
    },
    {
        "id": "r59",
        "pagina": 196,
        "texto": """La crítica de la frenología nos lleva a una conclusión importante: la razón no puede encontrarse a sí misma en el mundo de los objetos, porque ella misma es el principio de ese mundo. La razón no es una cosa entre las cosas; es la actividad que pone y supera las cosas. Por tanto, la razón debe dejar de observar y comenzar a actuar. Debe dejar de buscar su esencia en el mundo y debe empezar a producir su esencia en el mundo. Este es el paso a la razón práctica, a la razón que realiza su libertad en el mundo.

La razón observante ha recorrido un largo camino: ha observado la naturaleza, lo orgánico, la autoconciencia en sus leyes lógicas y psicológicas, y finalmente ha llegado a la frenología, donde se ha visto a sí misma como un hueso. Esta experiencia es necesaria: la razón debe aprender que no puede encontrarse a sí misma en el ser, sino solamente en el hacer. La verdad de la razón no es la contemplación, sino la acción. Con esto, pasamos a la siguiente sección: la realización de la autoconciencia racional."""
    },
    {
        "id": "r60",
        "pagina": 196,
        "texto": """evidentemente, que el cráneo, al igual que cualquier otro hueso, ha tenido propia formación viva, por lo cual, así considerado, es más bien él el que presiona sobre el cerebro y da a éste su delimitación externa, para lo que se presta también por ser el más duro de los dos. Pero, aun con ello, la determinación de la actividad entre ambos se mantendría dentro de la misma relación; pues el hecho de que el cráneo sea lo determinante o lo determinado no hace cambiar para nada la conexión causal; únicamente que, entonces, el cráneo pasaría a ser el órgano inmediato de la autoconciencia, ya que en él se encontraría como causa el lado del ser para sí. Sin embargo, en cuanto que el ser para sí, como vitalidad orgánica, recae en ambos del mismo modo, desaparecería entre ellos, de hecho, la conexión causal. Este desarrollo de ambos respondería a una conexión interior y sería una armonía orgánica preestablecida que dejaría a los dos lados relacionados entre sí libres el uno con respecto al otro, dejando a cada uno de ellos su propia figura, a la que no necesitaría corresponder la figura del otro; ni, con mayor razón, la figura y la cualidad del uno con respecto a las del otro, a la manera como son libres entre sí la forma de la uva y el sabor del vino. Pero, como la determinación del ser para sí cae del lado del cerebro y la determinación del ser allí del lado del cráneo, hay que establecer también una conexión causal entre ellos dentro de la unidad orgánica; una relación necesaria entre ellos como lados exteriores el uno al otro; es decir, una relación a su vez exterior, por medio de la cual, por tanto, la figura de uno sería determinada por la del otro, y viceversa."""
    },
    {
        "id": "r61",
        "pagina": 197,
        "texto": """Pero, en lo que se refiere a la determinación en que el órgano de la autoconciencia sería causa activa con respecto al lado contrapuesto, cabe hablar de muy diversas maneras, ya que en estos modos de hablar se trata de la contextura de una causa considerada en cuanto a su ser allí indiferente, su figura y su magnitud, de una causa cuyo interior y ser para sí deben ser tales que no afecten para nada al ser allí inmediato. La autoformación orgánica del cráneo es, en primer lugar, indiferente con respecto a la influencia mecánica, y la relación que media entre estas dos relaciones, puesto que la primera es el relacionarse consigo misma, es cabalmente esta misma indeterminabilidad y carencia de límites. Además, aun cuando el cerebro acogiese en sí las diferencias del espíritu como diferencias que son y fuese una pluralidad de órganos internos que ocupasen diferente espacio —lo que contradice a la naturaleza, que da a los momentos del concepto una existencia propia y, por tanto, pone la simplicidad fluida de la vida orgánica puramente en uno de los lados y la articulación y división de ella, con sus diferencias, en el otro lado, de tal modo que estas diferencias, tal como aquí deben ser entendidas, muestran como cosas anatómicas particulares—, según señala indeterminado si un momento espiritual, según que fuese originariamente más fuerte o más débil, tuviera necesariamente que poseer, en el primer caso, un órgano cerebral más extraño y en el segundo más contrario, o si no tendría que ser más bien a la inversa. Y otro tanto cabría decir acerca de si el desarrollo del momento espiritual agranda o empequeñece el órgano, lo hace más pesado y más espeso o, por el contrario, más fino. Y, al permanecer indeterminada la contextura de la causa, quedará también indeterminada la manera como se ejerce la influencia sobre el cráneo, si dilatándolo o estrechándolo y contrayéndolo. Aunque determinaremos esta influencia, tal vez, con mayor precisión que como un estímulo, seguirá siendo indeterminado si actúa a la manera de un emplasto de cantáridas, inflamatoriamente, o a la manera del vinagre, con acción reductoria. Para cada uno de estos pareceres cabría encontrar fundamentos plausibles, ya que la relación orgánica que en todos los casos interviene aquí permite tanto el uno como el otro y es indiferente con respecto a todo este entendimiento."""
    },
    {
        "id": "r62",
        "pagina": 198,
        "texto": """Pero la conciencia observadora no tiene por qué preocuparse tratando de determinar esta relación. Pues lo que, en todo caso, se halla en uno de los lados no es el cerebro como parte animal, sino el cerebro como ser de la individualidad consciente de sí. Esta, como carácter permanente y obrar consciente que se mueve a sí mismo, es para sí y en sí; a este ser para y en sí se enfrenta su realidad y su ser allí para otro; el ser para y en sí es la esencia y el sujeto que tiene en el cerebro un ser, que es subsumido bajo aquella esencia y que sólo cobra su valor por medio de la significación inmanente. Pero el otro lado de la individualidad consciente de sí, el lado de su existencia, es el ser como independiente y como sujeto, o como una cosa, a saber, un hueso; la realidad y el ser allí del hombre es su hueso craneano. He ahí la relación y el entendimiento que los dos lados de esta conexión tienen en la conciencia que los observa.

Ahora, esta conciencia tiene que ocuparse de la relación más determinada entre los dos lados; el hueso craneano tiene sin duda, en general, la significación de ser la realidad inmediata del espíritu. Pero la multilateralidad del espíritu da a su ser allí la correspondiente multivocidad; lo que se trata de obtener es la determinabilidad de la significación de los distintos lugares en que se divide este ser allí; y es necesario ver cómo en ellos se contiene la referencia a dicha significación. El cráneo no es un órgano de actividad, ni es tampoco un movimiento que hable; no se roba, se asesina, etc. con el cráneo, ni cuando se cometen estos actos se altera su gesto en lo más mínimo, como en un gesto elocuente. Y este que es no tiene tampoco el valor de un signo. El semblante y el gesto, el tono de voz, como la columna o el poste plantados en una isla desierta, anuncian en seguida que tratan de suponer algo distinto de aquello que sólo de un modo inmediato son. Ellos mismos se manifiestan inmediatamente como signos, en cuanto encierran una determinabilidad que se remite a algo distinto por el hecho de que no les pertenece de un modo propio y peculiar. También, a la vista de un cráneo como el de Yorik en Hamlet se pueden ocurrir diversas cosas; pero el hueso craneano, considerado como para sí, es una cosa tan indiferente, tan escueta, que en él, inmediatamente, no puede verse ni suponerse nada más que él mismo; recuerda, evidentemente, al cerebro y su determinabilidad, al cráneo de otra formación, pero no a un movimiento consciente, en cuanto que no lleva impreso en él un semblante ni un gesto, ni nada que se anuncie como emanado de un obrar consciente; pues es aquella realidad que debería presentar en la individualidad ese otro lado, el lado que no sería ya ser reflejado en sí mismo, sino un ser puramente inmediato."""
    },
    {
        "id": "r63",
        "pagina": 199,
        "texto": """Y como, además, el cráneo no se siente a sí mismo, parece desprenderse tal vez para él una significación más determinada a través de determinadas sensaciones que dieran a conocer por la vecindad lo que con el cráneo se supone; y en cuanto que un modo consciente del espíritu tiene su sentimiento en un determinado lugar del cráneo, tal vez esta zona indique, en su figura, ese modo del espíritu y su particularidad. A la manera como, por ejemplo, algunos, cuando concentran el pensamiento o, en general, cuando piensan, se quejan de sentir una tensión dolorosa en algún lugar de la cabeza, podría también ocurrir que el robar, el asesinar, el hacer poesía, etc., cada uno de estos actos, fuese acompañado de una sensación propia, que, además, debería estar localizada en una zona particular. Esta zona del cerebro, que de este modo se movería más y sería más activa, desarrollaría también, probablemente, más la zona vecina del cráneo; o bien ésta, por simpatía o por consenso, no permanecería inerte, sino que aumentaría o se reduciría o se modificaría del modo que fuese. Sin embargo, lo que hace esta hipótesis inversión es el hecho de que el sentimiento es, en general, algo indeterminado, y el sentimiento en la cabeza, en cuanto centro, podría ser el consentimiento universal de toda pasividad, de tal modo que con el cosquilleo o el dolor de cabeza del ladrón, el asesino o el poeta se mezclarían otros sentimientos que no sería fácil distinguir entre sí ni de otros que podrían llamarse meramente corpóreos, lo mismo que no es posible determinar la enfermedad por el síntoma del dolor de cabeza, si restringimos su significación solamente a lo corpóreo.

En efecto, por cualquier lado que consideremos la cosa, desaparece toda relación mutua necesaria, como desaparece también toda indicación expresada por sí misma. Resta solamente, como necesaria, si la relación ha de establecerse, una libre armonía preestablecida carente de concepto en la correspondiente determinación de ambos lados, ya que uno de ellos tiene que ser realidad carente de espíritu, una mera cosa. Se hallarán, pues, cabalmente, de un lado, una multitud de zonas estáticas del cráneo y, de otro, una multitud de propiedades del espíritu, cuya variedad y determinación dependerán del estado de la psicología. Y cuanto más pobre sea la representación del espíritu, más facilitada se verá por este lado la cosa; pues, de una parte, menor será el número de las propiedades y, de otra, más aisladas, fijas y osificadas serán estas propiedades del espíritu y, de este modo, tanto más parecidas a las determinaciones óseas y tanto más comparables a ellas. Sin embargo, aunque se facilite en mucho por esta pobreza de la representación del espíritu, siempre quedará en ambos lados una cantidad muy grande de determinaciones, y ello hará que permanezca para la observación la contingencia total de sus relaciones."""
    },
    {
        "id": "r64",
        "pagina": 200,
        "texto": """Si cada uno de los hijos de Israel tuviera que tomar de las arenas del mar, a las que todos ellos debían corresponder, el grano de arena del que es símbolo, la indiferencia y arbitrariedad que asignarían a cada uno de ellos el suyo serían tan grandes como las que suelen asignar a cada capacidad del alma, a cada pasión y a lo que también habría que tomar en consideración aquí, a los matices de los caracteres, de que acostumbran a hablar la psicología más sutil y el más sutil conocimiento del hombre, sus zonas craneanas y sus formas óseas. El cráneo del asesino no tiene este órgano o este signo, sino esta protuberancia; pero este asesino tiene, además, multitud de otras propiedades y de otras protuberancias y tiene, junto a éstas, partes hundidas; se puede elegir entre las protuberancias y las depresiones. Y, a su vez, su propensión al asesinato puede relacionarse con tales o cuales protuberancias o depresiones y éstas, por su parte, con tales o cuales propiedades, las que sean, pues ni el asesino es solamente esta abstracción de un asesino ni tiene solamente un abultamiento y una depresión. Por tanto, las observaciones que acerca de esto se hacen tienen exactamente el mismo valor que la lluvia del tendero o del ama de casa en relación con la feria y con la ropa puesta a secar. El tendero y el ama de casa podrían hacer también la observación de que llueve siempre que pasa este vecino o se saca a la mesa el asado de cerdo. Lo mismo que la lluvia es indiferente a estas circunstancias, también para la observación es indiferente esta determinabilidad del espíritu con respecto a este ser determinado del cráneo. En efecto, de los dos objetos de este observar, el uno es un escueto ser para sí, una propiedad osificada del espíritu, lo mismo que el otro es un escueto ser en sí; y, siendo ambos cosas osificadas, cada uno de ellos es perfectamente indiferente con respecto a todo lo demás; a la gran protuberancia le es tan indiferente el que se halle en su vecindad un asesino como a éste el que la zona hundida se halle cerca de él."""
    },
    {
        "id": "r65",
        "pagina": 200,
        "texto": """Queda siempre, ciertamente, la posibilidad insalvable de que a una propiedad, pasión, etc. se halle conectada una protuberancia en cualquier zona. Cabe representarse al asesino con una gran protuberancia aquí, en esta zona del cráneo y al ladrón con otra allí. En este respecto, la frenología es todavía susceptible de una ampliación todavía mayor, pues por el momento parece limitarse solamente a la conexión de una protuberancia con una propiedad en el mismo individuo, de tal modo que éste posea ambas. Pero ya la frenología natural —pues necesariamente tiene que existir ésta, lo mismo que existe una fisiognomía natural— va más allá de este límite, no se limita a juzgar que un hombre astuto tiene una protuberancia grande como un puño detrás de la oreja, sino que se representa, además, que la esposa infiel tiene, no ella misma, sino su cónyuge, ciertas protuberancias en la frente. Del mismo modo, cabría representarse a quien vive bajo el mismo techo que el asesino o incluso a su vecino y, llevando la cosa más allá, a sus conclusiones, etc. con grandes protuberancias en cualquier zona del cráneo, del mismo modo que el coleóptero acariciado por el cangrejo que saltó sobre el asno y después, etc. Pero si la posibilidad se toma, no en el sentido de la posibilidad de la representación, sino de la posibilidad interna o del concepto, entonces el objeto es una realidad tal que es y debe ser una pura cosa y sin semejante significación, que sólo puede tener en la representación.

(γ) Las dotes y la realidad

Si, a pesar de la indiferencia de ambos lados, el observador se empeña, sin embargo, a la obra de determinar relaciones, basándose para ello, en parte, en el fundamento racional universal de que lo exterior es la expresión de lo interior, y en parte apoyándose en la analogía con los cráneos de los animales —que, aunque puedan tener, ciertamente, un carácter más simple que los humanos, es al mismo tiempo tanto más difícil decir cuál tienen, ya que para la representación de..."""
    },
    {
        "id": "r66",
        "pagina": 202,
        "texto": """cualquier hombre puede no resultar tan fácil adentrarse certeramente en la naturaleza de un animal—, el observador encontrará en la aseveración de las leyes que pretende haber descubierto una excelente ayuda en una diferencia que necesariamente tiene que saltarnos a la vista aquí. Se concederá, por lo menos, que el ser del espíritu no puede tomarse como algo sencillamente fijo e inmutable. El hombre es libre; se concederá que el ser originario es solamente un conjunto de dotes sobre las que el hombre puede mucho o que necesitan de circunstancias favorables para llegar a desarrollarse; es decir, que un ser originario del espíritu debe enunciarse también como algo que no existe como ser. Por tanto, si las observaciones se hallan en contradicción con aquello que a uno se le ocurre aseverar como ley; si se tratase del tiempo que hace coincidiendo con la feria o con la ropa puesta a secar, el tendero o el ama de casa podrían decir que debiera propiamente llover y que, sin embargo, se halla presente la disposición a ello; y lo mismo ocurre con las observaciones sobre el cráneo: con la observación de que este individuo debiera ser propiamente como el cráneo lo enuncia con arreglo a ley y de que tiene una disposición originaria, pero que no ha llegado a desarrollarse; esta cualidad no se halla presente, pero debiera estarlo. La ley y el deber ser se basan en la observación de la lluvia real y del sentido real en esta determinabilidad del cráneo; pero si la realidad no se halla presente, tanto vale la posibilidad vacía. Esta posibilidad, es decir, la no realidad de la ley establecida y, por ende, las observaciones que la contradicen, tienen que irrumpir cabalmente por el hecho de que la libertad del individuo y las circunstancias propicias al desarrollo son indiferentes con respecto al ser en general, tanto con respecto a este ser como interior originario cuanto como exterior osificado, y de que el individuo puede ser también algo distinto de lo que originariamente y en lo interior es y, con mayor razón aún, algo distinto de un hueso.

Estamos, por tanto, ante la posibilidad de que esta protuberancia o este hundimiento del cráneo sea tanto algo real como también solamente una disposición y una disposición, además, indeterminada con respecto a cualquier cosa, y de que el cráneo designe algo no real; vemos que conduce, como siempre, a una mala excusa y que puede invocar en contra de aquello que precisamente trata de sostener. Vemos que la suposición se ve conducida por la naturaleza de la cosa a decir lo contrario de lo que tiene por seguro, pero a decirlo de un modo carente de pensamiento; —a decir que por medio de este hueso se indica algo, pero también y del mismo modo que no se indica nada."""
    },
    {
        "id": "r67",
        "pagina": 203,
        "texto": """Lo que flota confusamente ante la suposición misma en esta excusa es el pensamiento verdadero, que cancela precisamente la suposición, de que el ser como tal no es en general la verdad del espíritu. Del mismo modo que ya la disposición es un ser originario que no toma parte en la actividad del espíritu, también el hueso es, a su vez, un ser de ese tipo. Lo que es sin la actividad espiritual es una cosa para la conciencia y hasta tal punto no es su esencia que es más bien lo contrario de ella y la conciencia sólo es real para sí mediante la negación y la cancelación de semejante ser. Por este lado, debe considerarse que se reniega totalmente de la razón cuando se quiere hacer pasar un hueso por el ser allí real de la conciencia; y eso es lo que se hace al considerarlo como lo exterior del espíritu, pues lo exterior es precisamente la realidad que es. Y de nada sirve decir que partiendo de este algo exterior no se hace sino inferir lo interior, que es algo distinto y que lo exterior no es lo interior mismo, sino solamente su expresión. En efecto, en la relación entre ambos recae precisamente del lado de lo interior la determinación de la realidad que se piensa y es pensada y del lado de lo exterior la de la realidad que es. Cuando, por tanto, se dice a un hombre: tú (tu interior) eres esto porque tu cráneo tiene tal o cual constitución, eso sólo quiere decir una cosa, y es que yo considero un hueso como tu realidad. La réplica a semejante juicio mediante una bofetada, a que nos referíamos a propósito de la fisiognomía, hace, ante todo, que las partes blandas pierdan su prestigio y sean desplazadas de su situación y sólo demuestra una cosa: que estas partes no son un en sí verdadero, no son la realidad del espíritu —aquí, la réplica debería ir, en rigor, hasta hundir el cráneo de quien así juzga, demostrando así de un modo tan de bulto como lo es su sabiduría que un hueso, para el hombre, no es nada en sí, y menos aún su verdadera realidad."""
    },
    {
        "id": "r68",
        "pagina": 203,
        "texto": """El tosco instinto de la razón consciente de sí rechazará sin examen semejante ciencia frenológica —rechazará este otro instinto observador de la razón que, habiendo llegado hasta el vislumbre del conocimiento, ha captado éste del modo carente de espíritu en que lo exterior es expresión de lo interior. Pero, cuanto más malo es el pensamiento menos resalta, a veces, en qué reside de un modo determinado su falla y tanto más difícil resulta aislarla. En efecto, el pensamiento se dice tanto más malo cuanto más pura y más vacía es la abstracción que vale como su esencia. Sin embargo, la oposición que aquí importa tiene como términos la individualidad consciente de sí y la abstracción de la exterioridad totalmente convertida en cosa, aquel ser interior del espíritu aprehendido como ser fijo y carente de espíritu, contrapuesto cabalmente a tal ser. Pero, con ello, la razón observadora parece haber llegado, en efecto, a su punto culminante, a partir del cual debe necesariamente abandonarse a sí misma e invertirse, ya que sólo lo absolutamente malo lleva en sí la necesidad inmediata de invertirse. Del mismo modo, puede decirse del pueblo judío que precisamente por hallarse directamente ante las puertas de la salvación es y ha sido el más reprobado de todos los pueblos; no es él mismo lo que en y para sí debiera ser, no es autoescencia, sino que la desplaza más allá de sí; y mediante esta enajenación se hace posible una existencia más alta, aquella en que podría recobrar en sí su objeto, existencia más alta que si hubiese permanecido quieto dentro de la inmediatez del ser; en efecto, el espíritu es tanto más grande cuanto mayor es la oposición de la que retorna a sí mismo; pero esta oposición la forma el espíritu en la superación de su unidad inmediata y en la enajenación de su ser para sí. Sin embargo, si semejante conciencia no llega a reflejarse, el término medio en que se mantiene es el vacío desventurado, por cuanto que lo que debería llenar ese vacío se ha convertido en un extremo rígido. Por donde esta última fase de la razón observadora es la peor de todas, pero ello mismo hace necesaria su inversión."""
    },
    {
        "id": "r69",
        "pagina": 204,
        "texto": """[Conclusion. La identidad de sociedad y razón]

Una ojeada de conjunto sobre la serie de relaciones que hemos venido considerando y que constituyen el contenido y el objeto de la observación muestra que ya en su primer modo, en la observación de las relaciones de la naturaleza inorgánica desaparece ante ella el ser sensible; los momentos de su relación se presentan como puras abstracciones y como conceptos simples que debieran estar firmemente unidos con el ser allí de las cosas, pero este ser allí se pierde, de tal modo que el momento se muestra como puro movimiento y como universal. Este proceso libre acabado en sí mismo retiene la significación de algo objetivo, pero surge como un uno; en el proceso de lo ingrávico, lo uno es lo interior no existente; y como uno existente es lo orgánico. Lo uno se enfrenta, como ser para sí o esencia negativa, a lo universal, se sustrae a esto y permanece libre para sí, de tal modo que el concepto, realizado [realisiert] solamente en el elemento de la singularización absoluta no encuentra en la existencia [Existenz] orgánica su verdadera expresión de ser allí como universal, sino que permanece algo exterior o, lo que es lo mismo, un interior de la naturaleza orgánica. El proceso orgánico sólo es libre en sí, pero no lo es para sí mismo; en el fin entra el ser para sí de su libertad, existe como otra esencia, como una sabiduría consciente de ella misma, que es fuera de aquél. La razón observadora se vuelve, por tanto, a esta sabiduría, al espíritu, al concepto existente como universalidad o al fin existente como fin; y su propia esencia es de ahora en adelante, para ella, el objeto."""
    },
    {
        "id": "r70",
        "pagina": 205,
        "texto": """Se vuelve primeramente hacia su pureza; pero, en tanto que es aprehensión del objeto que se mueve en sus diferencias como un algo que es, las leyes del pensamiento se convierten para ella en relaciones de lo permanente con lo permanente; ahora bien, como el contenido de estas leyes no es más que un conjunto de momentos, se pierden todas ellas en lo uno de la autoconciencia. Este nuevo objeto, tomado asimismo como lo que es, es la autoconciencia singular y fortuita; por tanto, el observar se mantiene dentro del espíritu supuesto y de la relación fortuita entre la realidad consciente y la inconsciente. El objeto es en sí solamente la necesidad de esta relación; por tanto, la observación lo aborda de cerca y compara su realidad volitiva y activa con su realidad reflejada en sí y que se limita a considerar, que es ella misma una realidad objetiva. Este exterior, aunque sea un lenguaje del individuo, que éste tiene en sí mismo, es, al mismo tiempo, como signo, algo indiferente con respecto al contenido que debiera designar, lo mismo que lo que se pone como el signo es indiferente con respecto a esto.

De este lenguaje mudable la observación retorna, por tanto, finalmente, al ser fijo y enuncia de acuerdo con su concepto que la exterioridad, no como órgano ni tampoco como lenguaje y como signo, sino como cosa muerta, es la realidad exterior e inmediata del espíritu. Lo que ha sido superado de la primerísima observación de la naturaleza inorgánica, a saber, el que el concepto debiera hallarse presente como cosa, es instaurada por este modo final de la observación de tal manera que convierte la realidad del espíritu mismo en una cosa o, expresado a la inversa, da al ser muerto la significación del espíritu. De este modo, la observación llega al punto de enunciar lo que era nuestro concepto de ella, a saber, que la certeza de la razón se busca a sí misma como realidad objetiva. No se trata de decir con ello, ciertamente, que el espíritu, que se representa como un cráneo, sea enunciado como cosa; en este pensamiento no debe ir implicado ningún materialismo, como se le llama, sino que el espíritu debe ser más bien algo distinto de este hueso; pero el que es no significa, a su vez, sino que es una cosa. Si el ser como tal o el ser cosa es predicado del espíritu, ello es, por tanto, la verdadera expresión de que el espíritu es algo tal como un hueso. Hay que considerar, por consiguiente, de la más alta importancia el que se haya encontrado la verdadera expresión del hecho de que se diga puramente del espíritu que es. Cuando, por lo demás, se dice del espíritu que es, que tiene un ser, que es una cosa, una realidad singular, no se supone con ello algo que pueda verse o tomarse en la mano, tropezarse con ello, etc., pero si se dice eso; y lo que en verdad se dice se expresa, por tanto, al decir que el ser del espíritu es un hueso."""
    },
    {
        "id": "r71",
        "pagina": 206,
        "texto": """Este resultado tiene, ahora, una doble significación, que es, en primer lugar, su significación verdadera, en la medida en que es un complemento del resultado del precedente movimiento de la autoconciencia. La autoconciencia desventurada se ha enajenado su independencia y ha pugnado para convertir su ser para sí en cosa. Ha retornado con ello de la autoconciencia a la conciencia, es decir, a la conciencia para la que el objeto es un ser, una cosa; pero esto, lo que es cosa, es la autoconciencia, es, por tanto, la unidad del yo y del ser, la categoría. En tanto que el objeto es determinado así para la conciencia, ella tiene razón. La conciencia, lo mismo que la autoconciencia, es en sí propiamente razón; pero solamente de la conciencia para la que el objeto se ha determinado como la categoría puede decirse que tiene razón —pero algo distinto de esto es todavía el saber qué es la razón. La categoría, que es la unidad inmediata del ser y de lo suyo, tiene necesariamente que recorrer ambas formas, y la conciencia observadora es precisamente aquella ante la que la categoría se presenta en la forma del ser. En su resultado, esta conciencia expresa aquello cuya certeza carente de conciencia es como proposición —como la proposición que radica en el concepto de la razón. Esta proposición es el juicio infinito según el cual el sí mismo es una cosa —un juicio que se supera a sí mismo. A través de este resultado se añade, por tanto, a la categoría, algo determinado, el que es esta oposición que se supera. La pura categoría, que es para la conciencia en la forma del ser o de la inmediatez, es el objeto todavía no mediado, solamente presente, y la conciencia un comportamiento asimismo no mediado. El momento de aquel juicio infinito es el tránsito de la inmediatez a la mediación o negatividad. Por tanto, el objeto presente se determina como un objeto negativo y la conciencia como la autoconciencia con respecto a él, o la categoría, que ha recorrido la forma del ser en el observar, se pone ahora en la forma del ser para sí; la conciencia no quiere ya encontrarse de un modo inmediato, sino hacerse surgir a sí misma a través de su actividad. Ella misma es para ella el fin de su obrar, mientras que en el observar solamente le importaban las cosas.

La otra significación del resultado es la que ya hemos considerado, la de la observación carente de concepto. Esta observación no sabe captarse y expresarse más que enunciando sin más como la realidad de la autoconciencia el hueso, tal y como éste se encuentra como cosa sensible, que, al mismo tiempo, no pierde su objetividad para la conciencia. Pero no tiene tampoco claridad alguna de conciencia acerca de esto que dice, y no capta su propósito en la determinabilidad de su sujeto y predicado y en la relación entre ellos, y menos aún en el sentido del juicio infinito que se resuelve a sí mismo y del concepto. En virtud de una autoconciencia del espíritu más profunda que se manifiesta aquí como una honestidad natural, se oculta más bien la ignominia del pensamiento escueto carente de concepto que consiste en tomar un hueso por la realidad de la autoconciencia y lo adorna, con la misma carencia de pensamiento, intercalando en él diversas relaciones de causa y efecto, de signo, órgano, etc., que aquí no tienen ningún sentido, y disimulando lo que esta proposición tiene de tajante mediante las distinciones que de ella se derivan."""
    },
    {
        "id": "r72",
        "pagina": 207,
        "texto": """Las fibras cerebrales y otras cosas por el estilo, consideradas como el ser del espíritu, son ya una realidad pensada, puramente hipotética —no la realidad que es allí, sentida, vista y verdadera; cuando son allí, cuando son vistas, son objetos muertos y ya no valen como el ser del espíritu. Pero la objetividad propiamente dicha debe ser una realidad inmediata, sensible, de tal modo que el espíritu es puesto en ella como muerto, como real —pues el hueso es lo muerto, en tanto que es en lo vivo mismo. El concepto de esta representación es que la razón es para ella misma toda sociedad, incluso la sociedad puramente objetiva misma; pero es esto en el concepto, o solamente el concepto es su verdad, y cuanto más puro sea el concepto mismo, más desciende y se degrada para convertirse en una vana representación, si su contenido es como representación y no como concepto —si el juicio que se supera a sí mismo no se toma con la conciencia de esta su infinitud, sino como una proposición permanente y su sujeto y predicado valen cada uno de ellos para sí, fijándose el sí mismo como sí mismo, la cosa como cosa, a pesar de que lo uno debe ser lo otro. La razón, esencialmente el concepto, se esconde de un modo inmediato en sí mismo y en su contrario, oposición que precisamente por ello se supera de un modo igualmente inmediato. Pero, ofreciéndose así como el sí mismo y como su contrario y manteniéndose así firmemente en el momento totalmente singular de este desdoblamiento, es aprehendida irracionalmente; y cuanto más puros sean los momentos de ella, más tajante será la manifestación de este contenido, el cual o bien será solamente para la conciencia o bien será ingenuamente enunciado por ella. La profundidad que el espíritu extrae del interior, pero que sólo empuja hasta llevarla a su conciencia representativa, para dejarla en ésta —y la ignorancia de esta conciencia acerca de lo que es lo que ella dice, es la misma conexión de lo elevado y lo ínfimo que la naturaleza expresa ingenuamente en lo viviente, al combinar el órgano de su más alta perfección, que es el órgano de la procreación, con el órgano urinario. El juicio infinito como infinito sería la perfección de la vida que se comprende a sí misma; en cambio, la conciencia de la vida que permanece en la representación se comporta como el orinar."""
    },
    {
        "id": "r73",
        "pagina": 208,
        "texto": """B. LA REALIZACIÓN DE LA AUTOCONCIENCIA RACIONAL POR SÍ MISMA

La autoconciencia ha encontrado la cosa como sí misma y se ha encontrado a sí misma como cosa; es decir, para la autoconciencia la cosa es en sí la realidad objetiva. No es ya la certeza inmediata de ser toda realidad, sino una certeza para la que lo inmediato en general tiene la forma de algo superado, de tal modo que su objetividad solamente vale como la superficie cuyo interior y esencia es la autoconciencia misma. Por tanto, el objeto con que ésta se relaciona de un modo positivo es una autoconciencia; este objeto es en la forma de la sociedad, es decir, es independiente; pero la autoconciencia tiene la certeza de que este objeto independiente no es algo extraño para ella; sabe, así, que es reconocida en sí por él; la autoconciencia es el espíritu que abriga la certeza de tener la unidad consigo misma en la duplicación de su autoconciencia y en la independencia de ambas. Esta certeza es la que ahora tiene que elevarse ante él a verdad; lo que vale para ella, el que sea en sí y en su certeza interior, debe entrar en su conciencia y llegar a ser para ella.

[1. La dirección inmediata del movimiento de la conciencia da sí; el reino de la ética]

Cuáles serán las estaciones universales de esta realización lo caracteriza ya, en general, la comparación con el camino recorrido hasta aquí. En efecto, lo mismo que la razón observadora repetía en el elemento de la categoría el movimiento de la conciencia, a saber, la certeza sensible, el percibir y el entendimiento, la razón recorrerá también de nuevo el doble movimiento de la autoconciencia y pasará de la independencia a su libertad. Primeramente, esta razón activa sólo es consciente de sí misma como un individuo y debe, como..."""
    },
    {
        "id": "r74",
        "pagina": 208,
        "texto": """tal, postular y hacer brotar su realidad en el otro; en segundo lugar, al elevarse su conciencia a universalidad, deviene razón universal y es consciente de sí como razón, como un en y para sí ya reconocido, que aúna en su pura conciencia toda autoconciencia; es la esencia espiritual simple, que, al llegar al mismo tiempo a la conciencia, es la sustancia real dentro de la cual las formas anteriores retoman como a su fundamento, de tal modo que sólo son, con respecto a éste, momentos singulares de su devenir, que aunque se desgajan y se manifiestan como figuras propias, de hecho sólo tienen ser allí y realidad en cuanto sostenidas por dicho fundamento, y sólo tienen su verdad en tanto que son y permanecen en él mismo.

Si tomamos en su realidad [Realität] esta meta que es el concepto que ha nacido ya para nosotros —a saber, la autoconciencia reconocida que tiene la certeza de sí misma en la otra autoconciencia libre y que tiene precisamente en ella su verdad— o si destacamos este espíritu todavía interior como la sustancia que ha llegado ya hasta su ser allí, se abre en este concepto el reino de la ética. Este no es, en efecto, otra cosa que la unidad espiritual absoluta de su esencia en la realidad independiente de los individuos; una autoconciencia en sí universal que es a sí tan real en otra conciencia, que tiene esta perfecta independencia o es una cosa para ella y que precisamente en esto es consciente de la unidad con el otro y sólo en esta unidad con esta esencia objetiva es autoconciencia. Esta sustancia ética en la abstracción de la universalidad es solamente la ley pensada, pero es también, de un modo no menos inmediato, autoconciencia real, o es el hábito ético. Y, a la inversa, la conciencia singular es solamente este uno que es, en tanto que es consciente de la conciencia universal en su singularidad como su propio ser, en cuanto que su obrar y su existencia son el hábito ético universal."""
    },
    {
        "id": "r75",
        "pagina": 209,
        "texto": """En la vida de un pueblo es donde, de hecho, encuentra su realidad [Realität] consumada el concepto de la realización de la razón consciente de sí, donde esta realización consiste en intuir en la independencia del otro la perfecta unidad con él o en tener por objeto como mi ser para mí esta libre sociedad de un otro previamente contrastado por mí, que es lo negativo de mí mismo. La razón se halla presente como la sustancia universal fluida, como la sociedad simple inmutable, que irradia en muchas esencias totalmente independientes como la luz irradia en las estrellas como innumerables puntos luminosos para sí, que en su absoluto ser para sí no sólo se disuelven en la simple sustancia impenitente, sino que son también para sí mismos; son conscientes de ser estas esencias independientes singulares por el hecho de que sacrifican su singularidad y de que esta sustancia universal es su alma y su esencia; del mismo modo que este universal es, a su vez, su acción como esencias singulares o la obra producida por ellas.

El obrar y afianzarse puramente singulares del individuo se refieren a las necesidades que éste tiene como esencia natural, es decir, como singularidad que es. Si incluso estas sus funciones más corrientes no se reducen a la nada, sino que tienen realidad, ello se debe al individuo universal que sostiene al individuo, al poder del todo el pueblo. Pero el individuo no encuentra, en general, en la sustancia universal solamente esta forma de subsistencia de su actuar, sino también, igualmente, su contenido; lo que el individuo hace es la capacidad y el hábito ético universales de todos. Este contenido, en tanto que se singulariza totalmente está, en su realidad, circunscrito dentro del actuar de todos. El trabajo del individuo para satisfacer sus necesidades es tanto una satisfacción de las necesidades de los otros como de las suyas propias, y sólo alcanza la satisfacción de sus propias necesidades por el trabajo de los otros. Así como el individuo lleva ya a cabo en su trabajo singular, inconscientemente, un trabajo universal, lleva a cabo, a su vez, el trabajo universal como un objeto consciente; el todo se convierte en obra suya como totalidad, obra a la que se sacrifica y precisamente así se recobra a sí mismo desde esta totalidad. No hay aquí nada que no sea recíproco, nada en que la independencia del individuo no cobre su significación positiva del ser para sí en la disolución de su ser para sí en la negación de sí mismo."""
    },
    {
        "id": "r76",
        "pagina": 210,
        "texto": """Esta unidad del ser para otro o del hacerse cosa y del ser para sí, esta sustancia universal, habla su lenguaje universal en las costumbres y leyes de su pueblo; pero esta esencia inmutable que es no es sino la expresión de la individualidad singular misma que parece contrapuesta a ella; las leyes expresan lo que cada singular es y hace; el individuo no sólo las reconoce como su sociedad objetiva universal, sino que se reconoce asimismo en ella, o se reconoce como singularizado en su propia individualidad y en cada uno de sus conciudadanos. Por tanto, solamente en el espíritu universal tiene cada uno la certeza de sí mismo, o sea la certeza de no encontrar en la realidad que es más que a sí mismo; está tan cierto de los otros como de sí. Intuyo en todos que son para sí mismos solamente esta esencia independiente, como lo soy yo; intuyo en ellos la libre unidad con los otros, de tal modo que ella es a través de mí lo mismo que a través de los otros; los intuyo a ellos como yo, y me intuyo a mí como ellos.

En un pueblo libre se realiza, por tanto, en verdad la razón; ésta es el espíritu vivo presente, en que el individuo no sólo encuentra expresado su destino, es decir, su esencia universal y singular, y la encuentra presente como coseidad, sino que el mismo es esta esencia y ha alcanzado también su destino. De ahí que los hombres más sabios de la antigüedad hayan formulado la máxima de que la sabiduría y la virtud consisten en vivir de acuerdo con las costumbres de su pueblo."""
    },
    {
        "id": "r77",
        "pagina": 211,
        "texto": """[2. El movimiento inverso contenido en esta dirección; la esencia de la moralidad]

Sin embargo, de esta dicha que consiste en haber alcanzado su destino y vivir en él ha salido fuera la autoconciencia, que primeramente sólo de un modo inmediato y de acuerdo con el concepto es espíritu, aunque también podríamos decir que aún no lo ha alcanzado, pues ambas cosas podrían decirse del mismo modo.

La razón tiene necesariamente que salir fuera de esta dicha; pues sólo en sí o de un modo inmediato es la vida de un pueblo libre la eticidad real [real], o es una eticidad que es, con lo cual este espíritu universal es también el mismo un espíritu singular y la totalidad de las costumbres y las leyes una sustancia ética determinada, que sólo en el momento superior, a saber, en la conciencia de su esencia, se despoja de la limitación, y sólo en este reconocimiento, pero no inmediatamente en su ser, tiene su verdad absoluta; en este ser es, en parte, una sustancia limitada y, en parte, la limitación absoluta consistente precisamente en que el espíritu es en la forma del ser.

Además, la conciencia singular, tal como tiene de un modo inmediato su existencia en la eticidad real [real] o en el pueblo, es una confianza firme, en la que el espíritu no se ha resuelto con sus momentos abstractos y que, por tanto, no se sabe tampoco como ser para sí como pura singularidad. Pero, cuando llega a este pensamiento, como necesariamente tiene que llegar, se pierde esta unidad inmediata con el espíritu o su ser en él, pierde su confianza; aislada para sí, la conciencia singular es para sí misma la esencia, y no ya el espíritu universal. El momento de esta singularidad de la autoconciencia es, ciertamente, en el espíritu universal mismo, pero sólo como una magnitud llamada a desaparecer, que, al surgir para sí, se disuelve también de un modo inmediato en aquél y llega a la conciencia solamente como confianza. Al ser fijado así —y todo momento, por ser un momento de la esencia, tiene necesariamente que llegar él mismo a presentarse como esencia—, el individuo se ha enfrentado a las leyes y a las costumbres; estas sólo son un pensa..."""
    },
    {
        "id": "r78",
        "pagina": 212,
        "texto": """bio, según éste, es la conciencia de la misma, una conciencia que ella sabe como su propia esencia; y en este sentido, sería este movimiento del devenir de la moralidad, de una figura superior a aquélla. Sin embargo, estas figuras constituyen, al mismo tiempo, solamente un lado de su devenir, a saber, aquel que cae en el ser para sí o en el que la conciencia supera sus fines, y no el lado con arreglo al cual surge de la sustancia misma. Y como estos momentos no pueden tener todavía la significación de ser convertidos en fines en oposición con la eticidad perdida, valen aquí, ciertamente, según su contenido espontáneo, y la meta hacia la que impulsan es la sustancia ética. Pero, al hallarse más cerca de nuestros tiempos, aquella forma de los mismos momentos bajo la que se manifiestan después que la conciencia ha perdido su vida ética y repite en su búsqueda aquellas formas, se los puede representar aquí más bien en la expresión de este modo.

La autoconciencia, que primero es solamente el concepto del espíritu, aborda este camino en la determinabilidad de ser ella misma la esencia como espíritu singular; y su fin es, por tanto, el de darse la realización como un singular y el de gozar de sí mismo como tal, en ella.

En la determinación de ser ella misma la esencia como lo que es para sí, esta autoconciencia es la negatividad del otro; en su conciencia, ella misma se enfrenta, por tanto, como lo positivo, a algo que ciertamente es, pero que tiene para ella la significación de algo que no es en sí; la conciencia se manifiesta escondida en esta realidad encontrada y en el fin que cumple mediante la superación de dicha realidad y que convierte en realidad en vez de aquélla. Pero su primer fin es su inmediato ser para sí abstracto o el intuirse a sí misma, como este individuo, en otro, o intuir otra autoconciencia como sí misma. La experiencia de lo que es la verdad de este fin eleva a la autoconciencia a un plano más alto y se convierte a partir de ahora en fin de ella, en cuanto que es al mismo tiempo universal y tiene la ley de un modo inmediato en ella misma. Pero, al cumplir esta ley de su corazón, experimenta que la esencia singular no se mantiene aquí, sino que el bien sólo puede cumplirse mediante el sacrificio de ella, y la autoconciencia deviene virtud. La experiencia que ésta hace no puede ser otra que la de que su fin está ya cumplido en sí, de que la dicha se encuentra de un modo inmediato en la acción misma y de que la misma acción es el bien. El concepto de toda esta esfera, de que la sociedad es el ser para sí del espíritu mismo, deviene su movimiento para la autoconciencia. Al encontrarlo, la autoconciencia es, pues, para sí misma realidad [Realitat], como indi..."""
    },
    {
        "id": "r79",
        "pagina": 214,
        "texto": """vidualidad que se expresa de modo inmediato, que no encuentra ya resistencia en una realidad contrapuesta y para la que solamente esta expresión misma es objeto y fin.

a. EL PLACER Y LA NECESIDAD

La autoconciencia, que se es a sí en general la realidad [Realität], tiene su objeto en ella misma, pero como un objeto que primeramente sólo tiene para sí y que no es aún algo que es; el ser se enfrenta a ella como una realidad otra que la suya; y aquélla tiende a intuirse como otra esencia independiente llevando a cabo plenamente su ser para sí. Este primer fin es llegar a ser consciente de sí, como esencia singular, en la otra autoconciencia o hacer a este otro sí mismo; la autoconciencia tiene la certeza de que en sí este otro es ya ella misma. En tanto se ha elevado a su ser para sí desde la sustancia ética y el ser quieto del pensamiento, deja tras sí como una sombra gris, llamada a desaparecer, la ley de lo ético y del ser allí, los conocimientos de la observación y la teoría; pues esto es más bien un saber de algo cuyo ser para sí y cuya realidad son otros que los de la autoconciencia. No ha penetrado en ello el espíritu que parece celestial de la universalidad del saber y el obrar, en el que enmudecen la sensación y el goce de la singularidad, sino el espíritu terrenal, para el que sólo vale como la verdadera realidad el ser que es la realidad de la conciencia singular.

Desprecia al entendimiento y a la ciencia,
Que son del hombre los supremos dones.
Se ha entregado en brazos del demonio
Y tiene necesariamente que perecer.*

Se precipita, pues, hacia la vida y lleva hacia su cumplimiento la pura individualidad, en la cual surge. Más que a construir su dicha, se entrega a tomarla y disfrutarla de un modo inmediato. Las sombras de la ciencia, las leyes y los principios, que son lo único que se interpone entre ella y su propia realidad desaparecen como una niebla carente de vida, que no puede asumirla con la certeza de su realidad [Realität]; la autoconciencia toma la vida como se cosecha un fruto maduro, que se ofrece a la mano del mismo modo que ésta lo toma.

* Cita ligeramente modificada de unos versos del Fausto de Goethe, parte Iª, escena de Fausto y el discípulo."""
    },
    {
        "id": "r80",
        "pagina": 214,
        "texto": """[1. El placer]

Su acción es solamente con arreglo a uno de sus momentos una acción de apetencia; no tiende a la cancelación de toda la esencia objetiva, sino solamente a la forma de su ser otro o de su independencia, que es una apariencia carente de esencia, pues en sí vale para la autoconciencia como la misma esencia o su mismedad. El elemento en el que subsisten, indiferentes e independientes el uno con respecto al otro, la apetencia y su objeto, es el ser allí vivo; el goce de la apetencia supera esta existencia, en tanto corresponde a su objeto. Pero aquí este elemento, que da a ambos realidad particular, es más bien la categoría, un ser que es esencialmente un ser representado; es, por tanto, la conciencia de la independencia —ya sea la conciencia natural o la conciencia educada en o para un sistema de leyes y que mantiene a los individuos cada uno para sí. En sí, esta separación no es para la autoconciencia, que sabe la otra como su propia mismedad. Llega, pues, al goce del placer, a la conciencia de su realización, en una conciencia que se manifiesta como independiente, o llega a la intuición de la unidad de ambas autoconciencias independientes. Alcanza su fin, pero experimenta precisamente en ello lo que es la verdad del mismo. Se concibe como esta esencia singular que es para sí, pero la realización de este fin es, a su vez, la superación de él; pues la autoconciencia no se convierte para sí misma en objeto como esta autoconciencia singular, sino más bien como unidad de sí misma y de la otra autoconciencia y, de este modo, como singular superado o como universal."""
    },
    {
        "id": "r81",
        "pagina": 215,
        "texto": """[2. La necesidad]

El placer gozado tiene, sin duda, la significación positiva de haber devenido sí mismo como autoconciencia objetiva, pero también la significación negativa de haberse superado a sí mismo; y, como la autoconciencia sólo concebía su realización en la primera de las dos significaciones, su experiencia entra como contradicción en su conciencia, donde la realidad alcanzada de su singularidad ve cómo es aniquilada por la esencia negativa, que, carente de realidad, se enfrenta vacía a aquélla y es, sin embargo, la potencia que la devora. Esta esencia no es otra cosa que el concepto de lo que esta individualidad es en sí. Sin embargo, ésta es todavía la más pobre figura del espíritu que se realiza a sí mismo; pues no es ante sí sino la abstracción de la razón o la inmediataz de la unidad del ser para sí y del ser en sí; su esencia sólo es, por tanto, la categoría abstracta. Sin embargo, no tiene ya la forma del ser inmediato, simple, como el espíritu observador, en que es el ser abstracto o, puesto como algo extraño, la coseidad en general. En esta sociedad entran, aquí, el ser para sí y la mediación. Por tanto, la individualidad surge, ahora, como un círculo cuyo contenido es la pura relación desarrollada de las esencialidades simples. La realización alcanzada por esta individualidad sólo consiste, por consiguiente, en que haya hecho salir este círculo de abstracciones del confinamiento de la autoconciencia simple al elemento del ser para ella o del despliegue objetivo. Por tanto, lo que en el placer que se goza se convierte para la autoconciencia en objeto como su esencia es el despliegue de aquellas esencialidades vacías, de la pura unidad, de la pura diferencia y de su relación; fuera de esto, el objeto que la individualidad experimenta como su esencia no tiene otro contenido. Es lo que se llama la necesidad; pues la necesidad, el destino, etc. es precisamente aquello de lo que no sabe decirse qué hace, cuáles son sus leyes determinadas y su contenido positivo, porque es el puro concepto absoluto mismo intuido como ser, la relación simple y vacía, pero incontenible e indestructible, cuya obra es solamente la nada de la singularidad. La necesidad es esta cohesión firme, porque lo coherente son las puras esencialidades o las abstracciones vacías; una sola es la pura unidad, la cual es la más sólida y única, sino solamente en relación con su contrario y que, por tanto, no pueden desglosarse. Se refieren a una a la otra por medio de su concepto, pues son los puros conceptos mismos; y esta relación absoluta y este movimiento abstracto constituyen la necesidad. Por tanto, la individualidad solamente singular que sólo empieza teniendo por contenido el concepto puro de la razón, en vez de haberse precipitado de la teoría muerta a la vida, lo que ha hecho más bien ha sido precipitarse solamente a la conciencia de la propia carencia de vida y sólo participa de sí como la necesidad vacía y extraña, como la realidad muerta."""
    },
    {
        "id": "r82",
        "pagina": 216,
        "texto": """[3. La contradicción en la autoconciencia]

El tránsito se opera de la forma del uno a la forma de la universalidad, de una abstracción absoluta a otra, del fin del puro ser para sí que ha rechazado la comunidad con otros, al puro contrario, que es con ello un ser en sí igualmente abstracto. Esto se manifiesta, así, de tal modo que el individuo se ha limitado a ir al fondo y la absoluta esquivez de la singularidad se pulveriza al chocar con la realidad, igualmente dura, pero continua. Por cuanto que el individuo es, como conciencia, la unidad de sí mismo y de su contrario, este ir al fondo sigue siendo para él, es su fin y su realización, lo mismo que la contradicción entre lo que para él era la esencia y lo que es la esencia en sí; el individuo experimenta el doble sentido que lleva implícito lo que obra, a saber, el haber tomado su vida; tomaba la vida, pero asía más bien con ello la muerte.

Este tránsito de su ser vivo a la necesidad carente de vida se manifiesta ante él, por tanto, como una inversión sin mediación alguna. Lo mediador tenía que ser aquello en que ambos lados formaban una unidad, en que la conciencia, por tanto, reconocía un momento en el otro, reconoció su fin y su obrar en el destino y su destino en su fin y su obrar, reconoció su propia esencia en esta necesidad. Pero esta unidad es para esta conciencia precisamente el placer mismo o el sentimiento simple, singular, y el tránsito del momento de este su fin al momento de su verdadera esencia es, para esta conciencia, un puro salto a lo contrapuesto; en efecto, estos momentos no se contienen y entrelazan en el sentimiento, sino solamente en el puro sí mismo, que es un universal o el pensamiento. La conciencia se ha convertido, pues, más bien en un enigma por medio de su experiencia, en la que debía devenir para él su verdad y las consecuencias de sus actos no son para él sus actos mismos; lo que le sucede no es para ella la experiencia de lo que es en sí, el tránsito no es un mero cambio de forma del mismo contenido y la misma esencia, representados una vez como contenido y esencia de la conciencia y otra vez como objeto o esencia intuida de sí misma. Por consiguiente, la necesidad abstracta vale, pues, como la potencia solamente negativa y no concebida de la universalidad, contra la que se estrella la individualidad.

Hasta aquí llega la manifestación de esta figura de la autoconciencia; el momento final de su existencia es el pensamiento de su pérdida en la necesidad o el pensamiento de ella misma como una esencia absolutamente extraña a sí. Pero la autoconciencia ha sobrevivido en sí a esta pérdida; pues esta necesidad o esta pura universalidad es su propia esencia. Esta reflexión de la conciencia en sí, la necesidad de saberse como sí misma, es una nueva figura de la autoconciencia."""
    },
    {
        "id": "r83",
        "pagina": 217,
        "texto": """b. LA LEY DEL CORAZÓN Y EL DESVARÍO DE LA INFATUACIÓN

Lo que en verdad es la necesidad en la autoconciencia es lo que ella es para su nueva figura, en la que es ella misma como lo necesario; sabe que tiene inmediatamente en sí lo universal o la ley, la cual, en virtud de esta determinación según la cual es de modo inmediato en el ser para sí de la conciencia, se llama la ley del corazón. Esta figura, al igual que la anterior, es para sí, como singularidad, esencia; pero es más rica por la determinación según la cual este ser para sí vale para ella como necesaria o universal.

Así, pues, la ley que es de modo inmediato lo propio de la autoconciencia o un corazón, pero que tiene en él una ley, es el fin que esta autoconciencia tiende a realizar. Y hay que ver si su realización corresponderá a este concepto y si la autoconciencia experimentará en ella esta ley suya como la esencia.

[1. La ley del corazón y la ley de la realidad]

A este corazón se enfrenta una realidad; pues en el corazón la ley comienza siendo solamente para sí, aún no se ha realizado y es, por tanto, al mismo tiempo, algo otro que el concepto. Y este otro se determina así como una realidad que es lo contrapuesto a lo que ha de realizarse y, con ello, la contradicción de la ley y de la singularidad. Es, por tanto, de una parte, una ley que oprime a la individualidad singular, un orden del mundo violento que contradice a la ley del corazón, y, de otra parte, una humanidad que padece bajo ese orden y que no sigue la ley del corazón, sino que se somete a una necesidad extraña. Esta realidad, que se manifiesta frente a la figura actual de la conciencia, no es, como claramente se ve, otra cosa que la anterior relación desdoblada de la individualidad y de su verdad, la relación de una cruel necesidad opresora de la individualidad. Por eso, para nosotros, el movimiento anterior se enfrenta a la nueva figura, porque, habiendo brotado ésta en sí de él, el momento de que proviene es, por tanto, necesario para ella; pero ante ella este momento se manifiesta como algo previamente encontrado, ya que ella no tiene ninguna conciencia de su origen y la esencia ante ella es más bien el ser para sí misma o el ser lo negativo con respecto a este en sí positivo.

Esta individualidad tiende, pues, a superar esta necesidad que contradice a la ley del corazón, al igual que el padecer provocado por ella. Esto hace que la individualidad no sea ya la frivolidad de la figura anterior, que sólo apetece el placer singular, sino la seriedad de un fin elevado, que busca su placer en la presentación de su propia esencia excelente y en el logro del bien de la humanidad. Lo que ella realiza es la ley misma y su placer es, por tanto, al mismo tiempo, el placer universal de todos los corazones. Ambas cosas son inseparables para ella: su placer lo ajustado a la ley, y la realización de la ley de la humanidad universal la preparación de su..."""
    },
    {
        "id": "r84",
        "pagina": 218,
        "texto": """placer singular. En efecto, dentro de ella misma son una unidad, de modo inmediato, la individualidad y lo necesario; la ley es ley del corazón. La individualidad aún no se ha desplazado de su sitio, y la unidad de ambos no se ha realizado aún a través del movimiento mediador entre ellos, no es todavía el producto de la disciplina. La realización de la esencia inmediata no disciplinada vale como la presentación de su excelencia y como el logro del bien de la humanidad.

Por el contrario, la ley que se opone a la ley del corazón se halla separada del corazón y es una ley libre para sí. La humanidad que le pertenece no vive en la venturosa unidad de la ley con el corazón, sino en un estado cruel de escisión y sufrimiento o, por lo menos, de privación del goce de sí misma en el acatamiento de la ley y de falta de conciencia de la propia excelencia en su transgresión. Por hallarse aquel orden coercitivo divino y humano escindido del corazón, es para éste una apariencia llamada a perder lo que todavía conserva asociado a él: el poder y la realidad. Puede, en cuanto a su contenido, coincidir tal vez, de un modo contingente, con la ley del corazón, en cuyo caso ésta pueda tolerarlo; pero lo esencial, para él, no es el puro ajustarse a la ley como tal, sino el hecho de que el corazón encuentre en ello la conciencia de sí mismo, que él se satisfaga en ello. Allí donde el contenido de la necesidad universal no coincida con el corazón, tampoco en cuanto a su contenido será nada en sí y deberá ceder a la ley del corazón."""
    },
    {
        "id": "r85",
        "pagina": 219,
        "texto": """[2. La introducción del corazón en la realidad]

El individuo cumple, pues, la ley de su corazón; ésta deviene orden universal, y el placer se convierte en una realidad en y para sí conforme a ley. Pero, en esta realización, la ley ha huido, de hecho, del corazón; se ha convertido de modo inmediato simplemente en la relación que debía ser superada. La ley del corazón deja de ser ley del corazón precisamente al realizarse. En efecto, cobra en esta realización la forma del ser y es ahora una potencia universal para la que este corazón es indiferente, por donde el individuo, por el hecho de establecer su propio orden, deja de encontrarlo como el orden suyo. Por tanto, con la realización de su ley no hace surgir su ley, sino que, en tanto que la realización es en sí la suya y es, no obstante, para él una realización extraña, lo que hace es enredarse en el orden real, en un orden que es para él, además, una potencia superior no sólo extraña, sino incluso hostil. Con su obrar, el individuo se pone en o, mejor dicho, como el elemento universal de la realidad que es, y sus actos deben ellos mismos, con arreglo a su sentido, tener el valor de un orden universal. Pero, con ello, el individuo queda libre de sí mismo, se desarrolla para sí como universalidad y se depura de la singularidad; el individuo que sólo quiere reconocer la universalidad bajo la forma de su inmediato ser para sí no se reconoce, por tanto, en esta libre universalidad, a la vez que, sin embargo, pertenece a ella, pues es su obrar. Este obrar tiene, por tanto, la significación inversa de contradecir al orden universal, pues sus actos deben ser actos de su propio corazón singular, y no una realidad universal libre; y, al mismo tiempo, el individuo ha reconocido, de hecho, esta realidad universal, ya que el obrar tiene el sentido de poner su esencia como realidad libre, es decir, de reconocer la realidad como su propia esencia."""
    },
    {
        "id": "r86",
        "pagina": 220,
        "texto": """Mediante el concepto de su obrar, el individuo ha determinado más de cerca el modo como se vuelve contra él la universalidad real a la que se ha entregado. Sus actos pertenecen como realidad a lo universal; pero el contenido de ellos es la propia individualidad, que pretende mantenerse como este singular contrapuesto a lo universal. No se trata, aquí, de establecer una ley determinada cualquiera, sino que es la unidad inmediata del corazón singular con la universalidad lo que debe elevarse a ley y el pensamiento que debe tener validez: en lo que es ley tiene que reconocerse a sí mismo todo corazón. Pero, solamente el corazón de este individuo ha puesto su realidad en sus actos, que expresan para él su ser para sí o su placer. Estos actos deben valer de un modo inmediato como lo universal; es decir, son en verdad algo particular, que reviste solamente la forma de la universalidad: su contenido particular debe, como tal, valer en tanto que universal. De ahí que los demás no encuentren plasmada en este contenido la ley de su corazón, sino más bien la de otro; y precisamente con arreglo a la ley universal según la cual todos deben encontrar su corazón en lo que es ley, se vuelven contra la realidad que este individuo propone lo mismo que se volvían contra la suya propia. Y así como, primeramente, el individuo abominaba solamente de la ley rígida, ahora encuentra contrarios a sus excelentes intenciones los corazones mismos de los hombres, y abomina de ellos."""
    },
    {
        "id": "r87",
        "pagina": 221,
        "texto": """En cuanto que esta conciencia sólo conoce la universalidad como inmediata y la necesidad como necesidad del corazón, desconoce la naturaleza de la realización y de la eficiencia, desconoce que la realización, como lo que es, es en su verdad más bien lo universal en sí, en lo que desaparece la singularidad de la conciencia que se confía a ella para ser esta singularidad inmediata; por tanto, en vez de este su ser alcanza en el ser la enajenación de sí misma. Pero, aquello en que no se reconoce no es ya la necesidad muerta, sino la necesidad como animada por la individualidad universal. Tomaba este orden divino y humano que encontraba vigente por una realidad muerta en la cual, no sólo ella misma, que se fija como este corazón que es para sí y contrapuesto a lo universal, sino tampoco los otros, pertenecientes a este orden, tendrían la conciencia de ellos mismos; por el contrario, encuentra a este orden animado por la conciencia de todos y como ley de todos los corazones. Hace la experiencia de que la realidad es un orden animado, y lo experimenta precisamente en el obrar, precisamente por el hecho de que realiza la ley de su corazón; en efecto, esto no significa sino que la individualidad se convierte ella misma en objeto como universal, pero un objeto en el que no se reconoce."""
    },
    {
        "id": "r88",
        "pagina": 222,
        "texto": """[3. La rebelión de la individualidad, o el desvarío de la infatuación]

Por tanto, lo que para esta figura de la autoconciencia brota de su experiencia como lo verdadero contradice a lo que ella es para sí. Ahora bien, lo que ella es para sí tiene ello mismo, para esta figura, la forma de la universalidad absoluta, y es la ley del corazón que esto forme una unidad inmediata con la autoconciencia. Al mismo tiempo, el orden subsistente y vivo es, asimismo, su propia esencia y su propia obra, no hace surgir nada fuera de este orden; y forma igualmente una unidad inmediata con la autoconciencia. Esta pertenece, así, a una esencialidad duplicada y contrapuesta, contradictoria en sí misma y estremecida en lo más íntimo. La ley de este corazón es solamente aquella en que la autoconciencia se reconoce a sí misma. Pero el orden universal vigente ha devenido también, mediante la realización de aquella ley, su propia esencia y su propia realidad; por tanto, lo que en su conciencia se contradice es en ambos casos, para ella, bajo la forma de la esencia y de su propia realidad.

Por cuanto que la conciencia de sí expresa este momento de su decadencia consciente y en él el resultado de su experiencia, se muestra como esta inversión interior de sí misma, como la demencialidad de la conciencia, para la que su esencia es de un modo inmediato no-esencia y su realidad de un modo inmediato no realidad. La demencialidad no puede considerarse como si, en general, algo carente de esencia se tuviese por esencial y algo no real por real, de tal modo que lo que para uno es esencial o real no lo fuese para otro y que la conciencia de la realidad y de la no realidad o de la esencialidad y la no esencialidad se bifurcasen. Cuando algo es, de hecho y en general, real y esencial para la conciencia, pero no lo es para mí,..."""
    },
    {
        "id": "r89",
        "pagina": 222,
        "texto": """tengo al mismo tiempo en la conciencia su nulidad, puesto que yo soy conciencia en general, la conciencia de su realidad —y en cuanto que ambas cosas se hallan fijadas, esto forma una unidad, que es el desvarío en general. Pero en esto solamente un objeto es demencial para la conciencia, y no la conciencia como tal, en y para sí misma. Pero, en el resultado de la experiencia a que aquí se ha llegado, la conciencia, en su ley, se ha hecho consciente de sí misma como de esto real; y, al mismo tiempo, por cuanto que esta misma esencialidad, esta misma realidad se le ha enajenado, se ha hecho consciente, como autoconciencia, como realidad absoluta, de su no realidad, o ambos lados valen para ella, con arreglo a su contradicción de un modo inmediato, como su esencia, que es, por tanto, demencial en lo más íntimo.

Las palpitaciones del corazón por el bien de la humanidad se truecan, así, en la furia de la infatuación demencial, en el furor de la conciencia de mantenerse contra su destrucción, y ello es así porque arroja fuera de sí la inversión que la conciencia misma es y se esfuerza en ver en ella un otro y en enunciarla como tal. Enuncia, por tanto, el orden universal como una inversión de la ley del corazón y de su dicha, manejada por sacerdotes fanáticos y orgiásticos déspotas y sus servidores, quienes, humillando y oprimiendo, tratan de resarcirse de su propia humillación, y como si ellos hubiesen inventado esta inversión, esgrimiéndola para la desventura sin nombre de la humanidad defraudada. Llevada de este desvarío demencial, la conciencia proclama la individualidad como lo determinante de esta inversión y esta demencia, pero una individualidad ajena y fortuita. Pero es el mismo corazón o la singularidad de la conciencia que pretende ser inmediatamente universal el causante de esta inversión y esta locura, y sus actos sólo consiguen que esta contradicción llegue a su conciencia. En efecto, la ley del corazón es para él lo verdadero, algo meramente supuesto, que no ha afrontado, como el orden vigente, la luz del día, sino que, lejos de ello, se derrumba al mostrarse ante ésta. Esta ley suya debía tener realidad; en ello, es fin y esencia para él la ley como realidad, como orden vigente; pero, de un modo inmediato, la realidad, precisamente la ley como orden vigente, es para él más bien la nulidad. Y lo mismo, su propia realidad, el corazón mismo como singularidad de la conciencia, es el mismo la esencia; pero, el fin que persigue es poner su realidad como lo que es; por consiguiente, lo que para él es inmediatamente esencia es más bien su sí mismo como no-singular, o lo que es para él el fin, como ley, y precisamente en ello como una universalidad, que él pueda ser para su conciencia misma. Este concepto suyo se convierte, mediante su obrar, en un objeto; por tanto, experimenta su sí mismo más bien como lo no-real y la no-realidad como su realidad. No se trata, pues, de una individualidad contingente y extraña, sino que, en sí, en todos los respectos es precisamente este corazón lo invertido y lo que invierte."""
    },
    {
        "id": "r90",
        "pagina": 224,
        "texto": """Pero, si la individualidad inmediatamente universal es lo invertido y lo que invierte, este orden universal, que es la ley de todos los corazones, es decir, de lo invertido, es en sí mismo y en igual grado lo invertido, como la furiosa demencialidad lo proclamaba. Este orden universal muestra ser la ley de todos los corazones, de una parte, en la resistencia que la ley de un corazón encuentra en los otros singulares. Las leyes subsistentes son defendidas contra la ley de un individuo, porque no son una necesidad carente de conciencia, vaga y muerta, sino universalidad y sustancia espirituales, en las que viven como individuos y son conscientes de ellos mismos aquellos en quienes esas leyes tienen su realidad; de tal modo que, aunque se quieren de este orden como si fuese en contra de la ley interior y aunque mantienen en contra de él las suposiciones del corazón, se atienen de hecho a él como a su esencia, y lo pierden todo cuando este orden se les arrebata o si ellos mismos se colocan fuera de él. Y, siendo precisamente en esto en lo que consisten la realidad y el poder del orden público, éste se manifiesta, por tanto, como la esencia igual a sí misma y universalmente animada, y la individualidad como la forma de él. Pero este orden es, de otra parte, lo invertido.

En efecto, por ser este orden la ley de todos los corazones y por ser todos los individuos, de modo inmediato, este universal, es dicho orden una realidad que sólo es la realidad de la individualidad que es para sí misma o del corazón. La conciencia que establece la ley de su corazón experimenta, por tanto, resistencia por parte de otros, porque esa ley contradice a las leyes también singulares de sus corazones; y éstos, en su resistencia, no hacen otra cosa que establecer y hacer válida su propia ley. Lo universal que está presente sólo es, por tanto, una resistencia universal y una lucha de todos contra todos, en la que cada cual trata de hacer valer su propia singularidad, pero sin lograrlo, al mismo tiempo, porque experimenta la misma resistencia y porque su singularidad es disuelta por las otras, y a la inversa. Así, pues, lo que parece ser el orden público no es sino este estado de hostilidad universal, en el que cada cual arranca para sí lo que puede, ejerce la justicia sobre la singularidad de los otros y afianza la suya propia, la que, a su vez, desaparece por la acción de las demás. Este orden es el curso del mundo, la apariencia de una marcha permanente, que sólo es una universalidad supuesta y cuyo contenido es más bien el juego carente de esencia del afianzamiento de las singularidades y su disolución."""
    },
    {
        "id": "r91",
        "pagina": 225,
        "texto": """Si consideramos estos dos lados del orden universal en su mutua relación, vemos que la última universalidad tiene por contenido la individualidad inquieta, para la que la suposición o la singularidad es ley, lo real no-real y lo no-real real. Pero es también, al mismo tiempo, el lado de la realidad del orden, pues es el lado al que pertenece el ser para sí de la individualidad. El otro lado es lo universal como esencia quieta, pero precisamente por ello sólo como un interior, del que no puede decirse que no sea nada, pero que no es, sin embargo, ninguna realidad y que sólo puede llegar a ser, a su vez, real mediante la superación de la individualidad que se ha arrogado la realidad. Esta figura de la conciencia, consistente en llegar a ser en la ley, en lo verdadero y bueno en sí, no como la singularidad, sino solamente como esencia, y el saber la individualidad como lo invertido y lo que invierte, debiendo, por tanto, sacrificar la singularidad de la conciencia, es la virtud.

c. LA VIRTUD Y EL CURSO DEL MUNDO

[1. La vinculación de la autoconciencia con lo universal]

En la primera figura de la razón activa, la autoconciencia era ella misma pura individualidad y frente a ella se hallaba la universalidad vacía. En la segunda, las dos partes de la contraposición tenían en ellas cada uno de los dos momentos, ley e individualidad; pero uno de ellos, el corazón, era su unidad inmediata y el otro su contraposición. Aquí, en la relación entre la virtud y el curso del mundo, ambos términos son, cada uno a su vez la unidad y contraposición de estos momentos o un movimiento de la ley y la individualidad, la una con respecto a la otra, pero un movimiento contrapuesto. Para la conciencia de la virtud lo esencial es la ley y la individualidad lo que hay que superar, tanto, por consiguiente, en su conciencia misma como en el curso del mundo. En aquella conciencia, la propia individualidad debe disciplinarse bajo lo universal, bajo lo que es en sí lo verdadero y el bien; pero permanece así todavía conciencia personal; la verdadera disciplina sólo es el sacrificio de la personalidad total, como garantía de que la conciencia no permanece todavía vinculada a singularidades. En este sacrificio singular, la individualidad es cancelada, al mismo tiempo, en el curso del mundo, pues es también un momento simple, común a ambos términos. En el curso del mundo, la individualidad se comporta de modo inverso..."""
    },
    {
        "id": "r92",
        "pagina": 225,
        "texto": """a como se ponía en la conciencia virtuosa, a saber, se hace esencia y, en cambio, supedita a sí misma el bien y lo verdadero en sí. Además, para la virtud el curso del mundo no es solamente este universal invertido por la individualidad, sino que el orden absoluto es también un momento común, aunque en el curso del mundo no se halla presente para la conciencia como realidad que es, sino que es solamente su esencia interior. Este orden absoluto no tiene, propiamente, que ser producido por la virtud, pues la producción es, como acción, conciencia de la individualidad, y ésta más bien tiene que ser superada; pero, mediante esta superación es, por así decirlo, como si se dejase lugar al en sí del curso del mundo para que éste pueda entrar en sí y para sí mismo en la existencia.

El contenido universal del curso real del mundo se ha dado ya; considerado más de cerca no es, a su vez, otra cosa que los dos movimientos precedentes de la autoconciencia. De ellos ha brotado la figura de la virtud; y, como esos movimientos son su origen, son anteriores a ella; pero la figura de la virtud tiende a superar su origen y a realizarse [realisieren] o a devenir para sí. El curso del mundo es, por tanto, de una parte, la individualidad singular que busca su placer y su goce, pero que al proceder así encuentra su decadencia y satisface de este modo lo universal. Pero esta satisfacción misma, al igual que los demás momentos de esta relación, son una figura y un movimiento invertidos de lo universal. La realidad es solamente la singularidad del placer y del goce y lo universal, en cambio, lo contrapuesto a ella, una necesidad que es sólo la figura vacía de lo universal, una reacción puramente negativa y una acción carente de contenido. El otro momento del curso del mundo es la individualidad, que pretende ser ley en y para sí y que, llevada de esta pretensión, trasforma el orden establecido; es cierto que la ley universal se mantiene en contra de esta infatuación y no surge ya como algo vacío y contrapuesto a la conciencia, no como una necesidad muerta sino como necesidad en la conciencia misma. Pero, cuando existe como la relación consciente de la realidad absolutamente contradictoria es la demencia; y cuando esa ley universal es como realidad objetiva es la inversibilidad en general. Lo universal se presenta, pues, evidentemente, en los dos lados, como la potencia de su movimiento; pero la existencia de esta potencia es sólo la inversión universal."""
    },
    {
        "id": "r93",
        "pagina": 226,
        "texto": """[2. El curso del mundo, como la realidad de lo universal en la individualidad]

De la virtud debe ahora recibir lo universal su verdadera realidad, mediante la superación de la individualidad, del principio de la inversión; el fin que persigue la virtud es, pues, el invertir de nuevo el curso invertido del mundo y hacer brotar su esencia verdadera. Esta esencia verdadera es, primeramente, en el curso del mundo, como su en sí; no es aún real, y la virtud, por tanto, se limita a creerlo. Esta creencia tiende a elevarla a algo visible, pero sin gozar de los frutos de su trabajo y de su sacrificio. En efecto, en tanto que es individualidad, es el acto de la lucha que entabla con el curso del mundo; pero su fin y su esencia verdadera es la conquista de la realidad del curso del mundo; la existencia del bien que de este modo se efectúa es, así, la cesación de su obrar o de la conciencia de la individualidad. Cómo se sostiene esta lucha misma, qué experimenta en ella la virtud y si el curso del mundo sucumbe por el sacrificio que la virtud asume, mientras que la virtud triunfa, son cosas que tienen que decidirse con arreglo a la naturaleza de las armas vivientes manejadas por los luchadores. Pues estas armas no son otra cosa que la esencia de los luchadores mismos, la cual surge solamente para ellos dos mutuamente. Sus armas se desprenden ya, así, de lo que en sí se halla presente en esta lucha.

Lo universal es, para la conciencia virtuosa, verdadero en la fe o en sí, no es aún una universalidad real, sino abstracta; en esta conciencia misma es como fin, y en el curso del mundo como interior. Y es cabalmente en esta determinación como lo universal se presenta en la virtud para el curso del mundo, pues la virtud quiere primero llevar a cabo el bien y no da todavía al bien mismo como realidad. Esta determinabilidad puede considerarse también de tal modo que, en tanto que el bien surge en la lucha contra el curso del mundo, se presente así como lo que es para un otro, como algo que no es en y para sí mismo, pues de otro modo no pretendería darse su verdad, ante todo, mediante el sojuzgamiento de su contrario. Que es primeramente para un otro significa lo mismo que antes se mostraba del bien en la consideración contrapuesta, a saber, que es primeramente una abstracción que sólo tiene realidad en la relación, y no en y para sí.

El bien o lo universal, tal como aquí surge, es aquello a que se llama dones, capacidades, fuerzas. Es un modo de ser de la espiritualidad en que esto se representa como un universal, que para ser animado y cobrar movimiento necesita del principio de la individualidad y tiene en ésta su realidad. Este principio, en tanto que es en la conciencia de la virtud, aplica bien este universal, pero en tanto que es en el curso del mundo lo aplica mal —es un instrumento pasivo gobernado por la mano de la libre individualidad, indiferente en cuanto al uso que de él se hace y del que puede también abusarse para hacer surgir una realidad que es su destrucción; una materia carente de vida y sin independencia propia, que puede conformarse de este modo o del otro, e incluso para su propia ruina."""
    },
    {
        "id": "r94",
        "pagina": 227,
        "texto": """Y, en tanto que este universal se halla del mismo modo a la disposición de la conciencia de la virtud y del curso del mundo, no es posible percatarse de si, así pertrechada, la virtud vencerá sobre el vicio. Las armas son las mismas; son estas capacidades y estas fuerzas. Es cierto que la virtud ha depositado su fe en la unidad original de su fin y de la esencia del curso del mundo, como un ardil para caer sobre las espaldas del enemigo en el transcurso de la lucha y llevar en sí a este fin a su consecución, de tal modo que, de hecho, para el caballero de la virtud su propio obrar y su lucha son, en rigor, una finta que él no puede tomar en serio —puesto que pone su verdadera fuerza en el hecho de que el bien es en y para sí mismo, es decir, se cumple por sí mismo—, finta que tampoco debe dejar que sea tomada en serio. Pues lo que vuelve contra el enemigo y encuentra vuelto contra sí y que expone a que se desgaste y se detiene tanto en él mismo como en su enemigo, no debe ser el bien mismo, por cuya preservación y cumplimiento lucha, sino que lo que aquí se expone son solamente los dones y capacidades indiferentes. Sin embargo, éstas no son, de hecho, otra cosa que precisamente aquel mismo universal carente de individualidad que debe mantenerse y realizarse por medio de la lucha. Pero, al mismo tiempo, este universal es ya realizado de un modo inmediato por el concepto mismo de la lucha; es el en sí, lo universal; y su realización sólo significa que es al mismo tiempo para un otro. Los dos lados más arriba indicados, con arreglo a cada uno de los cuales lo universal devenía una abstracción, no son ya, ahora, lados separados, sino que en la lucha y por medio de ella el bien aparece puesto al mismo tiempo en ambos modos. Pero la conciencia virtuosa entra en la lucha con el curso del mundo como con algo contrapuesto al bien; lo que el curso del mundo ofrece a la conciencia, en esta lucha, es lo universal, no sólo como universal abstracto, sino como un universal animado por la individualidad y que es para otro, o como el bien real. Así, pues, allí donde la virtud prende en el curso del mundo hace siempre blanco en aquellos puntos que son la existencia del bien mismo, el cual se halla inseparablemente confundido en todas las manifestaciones del curso del mundo como el en sí de él y tiene también su existencia en la realidad de la misma; el curso del mundo es, por tanto, invulnerable para la virtud. Y estas existencias [Existenzen] del bien y, con ello, relaciones inviolables, son todos los momentos que la virtud debería atacar en ella y sacrificar. El luchar sólo puede ser, por tanto, una fluctuación entre el mantener y el sacrificar; o más bien diríamos que no puede caber ni sacrificio de lo propio ni transgresión de lo extraño. La virtud no sólo se asemeja al combatiente que en la lucha sólo se preocupa de mantener su espada sin daños; y no sólo no puede emplear las suyas propias, sino que debe mantener también intactas las del adversario y protegerlas contra sí misma, ya que todas ellas son partes nobles del bien por el cual se ha lanzado a la lucha."""
    },
    {
        "id": "r95",
        "pagina": 228,
        "texto": """Por el contrario, para este enemigo la esencia no es el en sí, sino la individualidad; su fuerza es, por tanto, el principio negativo para el que nada hay de subsistente y absolutamente sagrado, sino que puede afrontar y soportar la pérdida de todo y cada uno. Esto hace que la victoria sea segura, tanto en él mismo como por medio de la contradicción en que su adversario se enreda. Lo que en la virtud es en sí el curso del mundo sólo es para él; éste es libre de todo momento que para la virtud es firme y al que se halla vinculada. El curso del mundo tiene un tal momento en su poder, por el hecho de que para él sólo vale como un momento que puede tanto superar como dejar subsistente; y con ello tiene también en su poder al caballero virtuoso firme en ese momento. Este no puede desembarazarse de él como de un manto en que se envolviese exteriormente y liberarse de él, dejándolo atrás, pues ese momento es para él la esencia que no puede entregarse.

Finalmente, por lo que se refiere al ardid por medio del cual puede el en sí bueno atacar astutamente por la espalda al curso del mundo, esta esperanza es en sí nula. El curso del mundo es la conciencia despierta, cierta de sí misma, que no se deja atacar por la espalda, sino que da frente a todos los lados, pues es de tal modo que todo es para él, que todo está ante él. En cambio, el en sí bueno lo es para su adversario y es, así, en la lucha que hemos visto; y en tanto que es no para él, sino en sí, es el instrumento pasivo de las dotes y capacidades, la materia carente de realidad; representando como existencia, sería una conciencia durmiente que permanecería atrás, no se sabe dónde."""
    },
    {
        "id": "r96",
        "pagina": 229,
        "texto": """[3. La individualidad, como la realidad de lo universal]

La virtud es vencida, pues, por el curso del mundo porque su fin es, de hecho, la esencia abstracta no-real y porque, con vistas a la realidad, su acción descansa sobre lo diferente, que reside solamente en las palabras. La virtud pretendía consistir en llevar al bien a la realidad mediante el sacrificio de la individualidad, pero el lado de la realidad no es, él mismo, sino el lado de la individualidad. El bien debería ser lo que es en sí y contraponerse a lo que es, pero el en sí más bien, tomado según su realidad y verdad, el ser mismo. El en sí es, ante todo, la abstracción de la esencia con respecto a la realidad; pero la abstracción es precisamente lo que no es verdadero, sino que sólo es para la conciencia; es decir es él mismo aquello que es llamado real; pues lo real es lo que esencialmente es para un otro, o es el ser. Pero la conciencia de la virtud descansa sobre esta diferencia entre el en sí y el ser, que no tiene verdad alguna. El curso del mundo debería ser la inversión del bien, porque tenía como principio la individualidad; sin embargo, ésta es el principio de la realidad, pues precisamente ella es la conciencia por medio de la cual lo que es en sí es también para un otro; el curso del mundo invierte lo inmutable, pero lo invierte, de hecho, desde la nada de la abstracción en el ser de la realidad.

El curso del mundo vence, pues, sobre lo que, por oposición a él, constituye la virtud; vence sobre la virtud para la que la abstracción carente de esencia es la esencia. Pero no vence sobre algo real [Reales], sino sobre la invención de diferencias que no lo son, sobre esas pomposas frases sobre el bien más alto de la humanidad y lo que atenta contra él, sobre el sacrificarse por el bien y el mal uso que se hace de los dones; —tales esencias y fines ideales se derrumban como palabras vacuas que elevan el corazón y dejan la razón vacía, que son edificantes, pero no edifican nada; declamaciones que sólo proclaman de un modo determinado este contenido: que el individuo que pretexta obrar persiguiendo tan nobles fines y que emplea tan excelentes tópicos se considera como una esencia excelente; —es una inflación que agranda su cabeza y la de otros; pero la agranda hinchándola de vacío. La virtud antigua tenía una significación segura y determinada, pues tenía su fundamento pleno de contenido en la sustancia del pueblo y como su fin un bien real ya existente; no iba, pues, dirigida contra la realidad como una inversión universal y contra un curso del mundo. En cambio, ésta que consideramos es una virtud que sale fuera de la sustancia, una virtud carente de esencia, una virtud solamente de la representación y de las palabras, privada de aquel contenido."""
    },
    {
        "id": "r97",
        "pagina": 230,
        "texto": """Esta vacuidad de la retórica en lucha contra el curso del mundo se pondría en seguida en evidencia si se debiera decir lo que su retórica significa; —por eso se la presupone como conocida. La exigencia de decir esto que es conocido se cumpliría bien con un nuevo torrente de retórica o bien se le contrapondría la referencia al corazón, que dice interiormente lo que aquello significa; es decir, se confesaría, de hecho, la impotencia de decirlo. La nulidad de dicha retórica parece haber adquirido también certeza, de un modo no consciente, en cuanto a la cultura de nuestra época, por cuanto ha desaparecido todo interés de toda la masa de aquella fraseología y del modo de pavonearse con ellos; pérdida que encuentra su expresión en el hecho de que sólo produce hastío.

Por tanto, el resultado que surge de esta contraposición consiste en que la conciencia se desembaraza como de un manto vacío de la representación de un bien en sí que no tendría aún realidad alguna. La conciencia ha hecho en su lucha la experiencia de que el curso del mundo no es tan malo como se veía, pues su realidad es la realidad de lo universal. Y, con esta experiencia, desaparece el medio de hacer surgir el bien mediante el sacrificio de la individualidad; pues la individualidad es precisamente la realización de lo que es en sí; y la inversión cesa de ser considerada como una inversión del bien, pues es más bien precisamente la inversión de éste, como mero fin en la realidad [Realitat]: el movimiento de la individualidad es la realidad de lo universal.

Pero, de hecho, se vence también de este modo y desaparece lo que se enfrentaba como curso del mundo a la conciencia de lo que es en sí. El ser para sí de la individualidad se contraponía allí a la esencia o a lo universal y se manifestaba como una realidad separada del ser en sí. Pero, en cuanto que se ha mostrado que la realidad es la unidad inseparable con lo universal, se demuestra que el ser para sí del curso del mundo, lo mismo que el en sí de la virtud sólo es un modo de ver, y nada más. La individualidad del curso del mundo puede muy bien suponer que sólo obra para sí o de un modo egoísta, es mejor de lo que ella supone, su obrar es al mismo tiempo un obrar que es en sí, un obrar universal. Cuando obra egoístamente, simplemente no sabe lo que hace; y cuando asegura que todos los hombres obran de modo egoísta, simplemente afirma que los hombres no tienen conciencia de lo que es el obrar. Cuando la individualidad obra para sí, esto es precisamente el hacer surgir a la realidad lo que primeramente no era más que lo que es en sí. Así, pues, el fin del ser para sí que se supone contrapuesto al en sí —sus vacuas mañas lo mismo que sus sutiles explicaciones, que saben poner de relieve por doquier el egoísmo, han desaparecido asimismo, al igual que el fin del en sí y su retórica."""
    },
    {
        "id": "r98",
        "pagina": 231,
        "texto": """Por tanto, el obrar y el afanarse de la individualidad es fin en sí mismo; el empleo de las fuerzas, el juego de sus exteriorizaciones es lo que les infunde vida a ellas, que de otro modo serían el en sí muerto; el en sí no es un universal no desarrollado, carente de existencia y abstracto, sino que él mismo es de un modo inmediato la presencia y la realidad del proceso de la individualidad.

C. LA INDIVIDUALIDAD QUE ES PARA SI REAL [REEL] EN Y PARA SÍ MISMA

La autoconciencia ha captado ahora el concepto de sí, que primeramente era sólo el que nosotros teníamos de ella, a saber, ha captado el concepto según el cual es en la certeza de sí misma toda realidad; y, a partir de ahora, el fin y la esencia es, para ella, la compenetración dotada de movimiento de lo universal —de las dotes y capacidades— con la individualidad. Los momentos singulares de esta plenitud y compenetración anterior a la unidad en la que se han conjuntado son los fines hasta aquí considerados. Han desaparecido como abstracciones y quimeras pertenecientes a aquellas primeras figuras huecas de la autoconciencia espiritual y que tienen su verdad solamente en el ser supuesto del corazón, de la presuntuosidad y las palabras, pero en la razón, que ahora, segura en y para sí de su realidad, no trata ya de hacerse surgir primeramente como fin por oposición a la realidad que inmediatamente es, sino que tiene como objeto de su conciencia la categoría como tal. Se ha superado, en efecto, la determinación de lo que es para sí o de la autoconciencia negativa, en que la razón aparecía; esa autoconciencia se encontraba con una realidad que sería lo negativo de ella misma y a través de cuya superación y sólo así realizaría su fin. Pero, por cuanto que fin y ser en sí han resultado ser lo mismo que el ser para otro y la realidad encontraría, la verdad no se separa ya de la certeza, dando lo mismo que el fin puesto se tome por la certeza de sí mismo y su realización por la verdad o que el fin se tome por la verdad y la realidad por la certeza; sino que la esencia y el fin es en y para sí mismo la certeza de la misma realidad [Realitat] inmediata, la compenetración del en sí y el para sí, de lo universal y la individualidad; el obrar es en él mismo su verdad y su realidad, y la presentación o la proclamación de la individualidad es para este obrar fin en y para sí mismo.

Con este concepto, la autoconciencia ha retomado, por tanto, a sí, desde las determinaciones contrapuestas que la categoría tenía..."""
    },
    {
        "id": "r99",
        "pagina": 231,
        "texto": """para ella y para su comportamiento, como autoconciencia primero observadora y luego activa. Ahora, tiene la pura categoría misma como su objeto, o es la categoría que ha devenido consciente de ella misma. Ha ajustado, pues, las cuentas con sus figuras anteriores; éstas nacen en el olvido tras ella y no se enfrentan como el mundo con que se ha encontrado, sino que se desarrollan solamente dentro de ella misma, como momentos transparentes. Sin embargo, en su conciencia se desdoblan todavía como un movimiento de momentos distintos, que aún no se han conjuntado en su unidad sustancial. Pero la conciencia de sí mantiene en todos ellos la unidad simple del ser y del sí mismo, unidad que es su género.

La conciencia se ha despojado, así, de toda oposición y de toda condición de su obrar; sale lozana fuera de sí, y no tiende hacia un otro, sino hacia sí misma. Por cuanto que la individualidad es la realidad en ella misma, la materia del actuar y el fin del obrar son en el obrar mismo. El obrar presenta, por tanto, el aspecto del movimiento de un círculo que por sí mismo se mueve libremente en el vacío, que tan pronto se amplía como se estrecha sin verse entorpecido por nada y que, perfectamente satisfecho, juega solamente en sí mismo y consigo mismo. El elemento en que la individualidad presenta su figura tiene la significación de limitarse puramente a acogerla; es simplemente la luz del día bajo la cual pretende mostrarse la conciencia. El obrar no altera nada ni va contra nada; es la pura forma de la traducción del no ser visto al ser visto, y el contenido que así sale a la luz y se presenta no es otra cosa que lo que tiene ya en sí este obrar. Es en sí; ésta es su forma como unidad pensada; y es real —ésta es su forma como unidad que es; él mismo es contenido solamente en esta determinación de la simplicidad con respecto a la determinación de su tránsito y de su movimiento.

### 4. EL REINO ANIMAL DEL ESPÍRITU Y EL ENGAÑO, O LA COSA MISMA

Esta individualidad en sí real sigue siendo, ante todo, una individualidad singular y determinada; la realidad absoluta como la que se sabe es, por tanto, tal como ella es consciente de sí, la realidad universal abstracta, que, sin cumplimiento y sin contenido, es solamente el pensamiento vacío de esta categoría. Debemos ver ahora cómo este concepto de la individualidad en sí misma real se determina en sus momentos y cómo le entra en la conciencia su concepto de ella misma.

[1. El concepto de la individualidad, como individualidad real]

El concepto de esta individualidad, como ella en tanto que tal es para..."""
    },
    {
        "id": "r100",
        "pagina": 233,
        "texto": """[1. El concepto de la individualidad, como individualidad real]

El concepto de esta individualidad, como ella en tanto que tal es para sí misma toda la realidad, es primeramente resultado; la individualidad no ha presentado aún su movimiento y su realidad [Realitat] y es puesta aquí de modo inmediato como simple ser en sí. Pero la negatividad, que es lo mismo que se manifiesta como movimiento, es en el simple en sí como determinabilidad; y el ser o el simple en sí deviene un determinado ámbito. La individualidad aparece, por tanto, como naturaleza originaria determinada, —como naturaleza originaria, porque es en sí, y como originaria determinada, porque lo negativo es en el en sí, y esto es por ello una cualidad. Sin embargo, esta limitación del ser no puede limitar la acción de la conciencia, pues ésta es aquí un perfecto relacionarse consigo misma; la relación con otro, que sería la limitación de la misma conciencia es superada. La determinabilidad originaria de la naturaleza es, por tanto, solamente principio simple, —un elemento universal transparente en el que la individualidad permanece libre e igual a sí misma, del mismo modo que despliega allí sin entorpecimiento sus diferencias y es pura relación mutua consigo misma en su realización. Lo mismo ocurre con la vida animal indeterminada, que infunde su hábito de vida, digamos, al elemento del agua, del aire o de la tierra y, en ellos, a su vez, a principios más determinados, imbuyendo en ellos todos sus momentos, pero manteniéndolos en su poder a despecho de aquella limitación del elemento y manteniéndose a sí misma en su uno, con lo que sigue siendo, en tanto que esta organización particular, la misma vida animal universal.

Esta naturaleza determinada originaria de la conciencia, en ella libre y totalmente permanente, se manifiesta como el contenido inmediato y el único propio de lo que para el individuo es el fin; es, ciertamente un contenido determinado, pero en general sólo es contenido en tanto que consideramos aisladamente el ser en sí; pero, en verdad, es la realidad [Realitat] penetrada por la individualidad, la realidad tal como la conciencia, como singular, la tiene en ella misma y que se pone primeramente como lo que es y no todavía como lo que actúa. Sin embargo, para el obrar aquella determinabilidad, de una parte, no es una limitación que trate de sobrepasar porque, considerada como cualidad que es, es el simple color del elemento en que se mueve; y, de otra parte, la negatividad sólo es determinabilidad en el ser; pero el obrar no es en sí mismo otra cosa que la negatividad; por tanto, en la individualidad que actúa la negatividad..."""
    },
    {
        "id": "r101",
        "pagina": 234,
        "texto": """de sí y una realidad que es fuera de ella. Sólo que para que sea para la conciencia lo que ello es en sí debe obrar, lo que vale tanto como decir que el obrar es precisamente el devenir del espíritu como conciencia. Lo que ella es en sí lo sabe, pues, por su realidad. Por tanto, el individuo no puede saber lo que es antes de traducirse en realidad mediante la acción. Parece, pues, según esto, que no pueda determinar el fin de su obrar antes de haber obrado; pero, al mismo tiempo, siendo conciencia, debe tener ante sí previamente el obrar como algo totalmente suyo, es decir, como fin. El individuo que se dispone a obrar parece encontrarse, por tanto, en un círculo en el que todo momento presupone ya el otro, sin poder encontrar, de este modo, un comienzo, ya que sólo aprende a conocer su esencia originaria, que debe ser su fin por el obrar, pero para obrar necesita tener ante sí, previamente, el fin. Precisamente para ello debe comenzar de un modo inmediato y pasar a la actividad bajo cualesquiera circunstancias, sin seguirse preocupando para nada del comienzo, el medio ni el final, pues su esencia y su naturaleza que es en sí lo es todo conjuntamente, comienzo, medio y final. Como comienzo, se halla presente en las circunstancias de la acción; y el interés que el individuo encuentra en algo es la respuesta ya dada a la pregunta de si hay algo que hacer aquí, y qué. En efecto, lo que parece ser una realidad previamente encontrada es en sí su naturaleza originaria, que sólo tiene la apariencia de un ser —una apariencia que radica en el concepto del obrar que se desdobla, pero que se proclama como su naturaleza originaria en el interés que encuentra en ella. Y asimismo el cómo o el medio es determinado en y para sí. Y el talento no es, igualmente, otra cosa que la determinada individualidad originaria, considerada como medio interior o como el tránsito del fin a la realidad. Pero el medio real y el tránsito real son la unidad del talento y de la naturaleza de la cosa presente en el interés; aquél presenta en el medio el lado del obrar, éste el lado del contenido, y ambos son la individualidad misma, como compenetración del ser y del obrar. Por tanto, lo que se halla presente son las circunstancias previamente encontradas, que son en sí la naturaleza originaria del individuo; en segundo lugar, el interés que aquélla pone precisamente como lo suyo o como fin y, por último, la conexión y superación de esta oposición en el medio. Esta conexión cae todavía por sí misma dentro de la conciencia y el todo que acabamos de considerar es un lado de esta oposición. Esta apariencia de contraposición que aún subsiste es superada por el tránsito mismo o por el medio; —pues es la unidad de lo exterior y lo interior, lo contrario de la determinabilidad que tiene como medio interior; la supera, por tanto, y se pone a sí, es..."""
    },
    {
        "id": "r102",
        "pagina": 236,
        "texto": """decir, esta unidad del obrar y del ser, asimismo como exterior, como la individualidad misma convertida en real, o sea como la individualidad puesta para sí misma como lo que es. De este modo, el obrar todo no brota de sí mismo ni como las circunstancias, ni como el fin, ni como el medio, ni como la obra.

Pero, con la obra parece introducirse la diferencia en cuanto a las naturalezas originarias; la obra es, como la naturaleza originaria que expresa, algo determinado; pues cuando el obrar la abandona y deja libre como realidad que es, se da en ella la negatividad en tanto que cualidad. Y la conciencia se determina, frente a ella, como lo que tiene en sí la determinabilidad como negatividad en general, como el obrar; es, por tanto, lo universal con respecto a aquella determinabilidad de la obra y puede, por consiguiente, ser comparada con otras y, partiendo de aquí, captar las individualidades mismas como diversas; puede captar al individuo que trasciende más ampliamente a su obra, bien como una energía más poderosa de la voluntad, bien como una naturaleza más rica, es decir, como una naturaleza cuya originaria determinabilidad es más limitada y otra, por el contrario, como una naturaleza más débil y más pobre.

Frente a esta diferencia no esencial de magnitud, lo bueno y lo malo expresarán una diferencia absoluta; pero ésta no encuentra lugar aquí. Lo que se tomará de un modo o de otro es del mismo modo un hacer y un obrar, el presentarse y el expresarse de una individualidad y, por consiguiente, todo será bueno y no podría decirse, propiamente hablando, qué debería ser lo malo. Lo que se llamaría una obra mala es la vida individual de una naturaleza determinada, que se realiza en ella; y sólo se convertiría y corrompería en una obra mala mediante el pensamiento comparativo, el cual, sin embargo, es algo vacío, porque va más allá de la esencia de la obra, que consiste en ser un expresarse de la individualidad que, fuera de esto, no se sabe lo que busca y postula en ella. Dicho pensamiento sólo podría afectar a la diferencia antes señalada; pero ésta es en sí, como diferencia de magnitud, una diferencia no esencial, que aquí es una diferencia determinada por el hecho de que serían comparadas entre sí diferentes obras o individualidades, pero éstas son indiferentes entre sí; cada una de ellas se refiere únicamente a sí misma. La naturaleza originaria es solamente el en sí o lo que podría tomarse como base en tanto que pauta de enjuiciamiento de la obra, y viceversa; pero ambas cosas se corresponden entre sí, para la individualidad no hay nada que no sea por ella o, lo que es lo mismo, no hay ninguna realidad que no sea su naturaleza y su obrar, y ningún obrar ni en sí de la individualidad que no sea real, y solamente estos momentos admiten comparación."""
    },
    {
        "id": "r103",
        "pagina": 237,
        "texto": """Aquí, no hay, pues, margen ni para exaltarse ni para lamentarse o arrepentirse; pues todo esto proviene del pensamiento que se imagina ser otro contenido y otro en sí que la naturaleza originaria del individuo y su desarrollo presente en la realidad. Sea lo que fuere lo que haga y lo que le ocurra, lo hará él y será él mismo; el individuo sólo puede tener la conciencia de la pura traducción de sí mismo de la noche de la posibilidad al día de la presencia, del en sí abstracto a la significación del ser real y tener la certeza de que lo que ante él aparece ahora a la luz del día no es otra cosa que lo que antes dormitaba en aquella noche. La conciencia de esta unidad es también, ciertamente, una comparación, pero lo que se compara sólo tiene, cabalmente, la apariencia de la oposición; una apariencia formal, que para la autoconciencia de la razón, según la cual la individualidad es en sí misma la realidad, no es más que una apariencia. Por tanto, el individuo sólo puede experimentar el goce de sí mismo, puesto que sabe que en su realidad no puede encontrar otra cosa que su unidad con él, es decir, solamente la certeza de sí mismo en su verdad y que, por tanto, siempre alcanza su fin.

[2. La cosa misma y la individualidad]

Tal es el concepto que se forma de sí la conciencia, que está cierta de sí misma como absoluta compenetración de la individualidad y del ser; veamos si este concepto se confirma por la experiencia y su realidad [Realitat] coincide con él. La obra es la realidad [Realitat] que se da la conciencia; es aquello en que el individuo es para la conciencia lo que es en sí, de tal modo que la conciencia para la cual el individuo deviene en la obra no es la conciencia particular, sino la conciencia universal, la conciencia, en la obra, trasciende en general al elemento de la universalidad, al espacio indeterminado del ser. La conciencia que se retrotrae de su obra es, de hecho, la conciencia universal, —porque deviene la negatividad absoluta o el obrar en esta oposición—, con respecto a su obra, que es lo determinado; la conciencia va, pues, más allá de sí misma en tanto que obra y es por sí misma el espacio indeterminado que no se encuentra lleno por su obra. Sin embargo, si antes su unidad se mantenía en el concepto, era precisamente por el hecho de que la obra era superada en tanto que obra que es. Pero la obra debe ser, y hay que ver cómo en su ser mantendrá la individualidad su universalidad y sabrá satisfacerse. Ante todo, hay que considerar para sí la obra que ha llegado a ser."""
    },
    {
        "id": "r104",
        "pagina": 238,
        "texto": """Esta obra ha recibido también toda la naturaleza de la individualidad; por tanto, su ser es él mismo un obrar en el que se compenetran y superan todas las diferencias; la obra es, por consiguiente, proyectada hacia afuera en una subsistencia en la que, de hecho, la determinabilidad de la naturaleza originaria se vuelve en contra de otras naturalezas determinadas y penetra en ellas, lo mismo que estas otras naturalezas se pierden en ella y se pierden en este movimiento universal como momento llamado a desaparecer. Si dentro del concepto de la individualidad real [reale] en y para sí misma son iguales entre sí todos los momentos y circunstancias, el fin y el medio y la realización y la naturaleza originaria determinada sólo vale como elemento universal, frente a esto y en cuanto que este elemento deviene ser objetivo, su determinabilidad como tal sale a la luz del día en la obra y adquiere su verdad en su disolución. Vista más de cerca, esta disolución se presenta de tal modo que en esta determinabilidad el individuo ha devenido real en tanto que este individuo; pero esta determinabilidad no es solamente contenido de la realidad, sino también forma de ella o, dicho en otros términos, la realidad como tal es en general la determinabilidad que consiste en contraponerse a la autoconciencia. Vista por este lado, se muestra como la realidad que ha desaparecido del concepto, simplemente como una realidad extraída previamente encontrada. La obra es, es decir, es para otras individualidades, y es para ellas una realidad extraña, en lugar de la cual deben ellas poner la suya propia, para que pueda darse por medio de su obrar la conciencia de su unidad con la realidad; en otras palabras, su interés en aquella obra, puesto por su naturaleza originaria, es otro que el interés peculiar de esta obra, que por ello mismo se convierte en algo distinto. La obra es, por tanto, en general, algo perecedero, que es extinguido por el juego contrario de otras fuerzas y otros intereses y que presenta más bien la realidad [Realitat] de la individualidad más bien como llamada a desaparecer que como consumada.

Para la conciencia nace, pues, en su obra la oposición entre el obrar y el ser, que en las figuras anteriores de la conciencia era, al mismo tiempo, el comienzo del obrar y que aquí es solamente resultado. Pero esta oposición se había tomado también, de hecho, como base en tanto que la conciencia procedía a obrar como la individualidad real [reale] en sí; pues el obrar presuponía la naturaleza originaria determinada como el en sí y tenía por contenido el puro consumarse por la consumación misma. Pero el puro obrar es la forma igual a sí misma, de la que difiere, por ello, la determinabilidad de la naturaleza originaria. Aquí, como en los otros casos, es indiferente, cuál de las dos cosas es llamada concepto y cuál realidad [Realität]; la naturaleza originaria es lo pensado o el en sí con respecto al obrar, en el cual cobra aquélla su realidad [Realität]; o, en otros términos, la naturaleza originaria es el ser tanto de la individualidad en tanto que tal como de ella en cuanto obra mientras que el obrar es el concepto originario como transición absoluta o como el devenir. Esta inadecuación entre el concepto y la realidad [Realität], que radica en su esencia, la experimenta la conciencia en su obra; en ésta deviene, por tanto, la conciencia como en verdad es, y el concepto vacío que tiene de sí misma desaparece."""
    },
    {
        "id": "r105",
        "pagina": 239,
        "texto": """En esta fundamental contradicción de la obra, que es la verdad de esta individualidad que se es real [reales] en sí, brotan así de nuevo como contradictorios todos los lados de la misma; o, dicho de otro modo, la obra, como el contenido de toda la individualidad, salida del obrar, que es la unidad negativa y retiene presos todos los momentos, colocada en el ser, pone ahora en libertad dichos momentos; y en el elemento de la subsistencia devienen indiferentes entre sí. Concepto y realidad [Realität] se separan, por tanto, como el fin y como lo que es la esencialidad originaria. El que el fin tenga verdadera esencia o el que el en sí se haga fin, es algo fortuito. Y asimismo vuelven a separarse el concepto y la realidad [Realität] como tránsito a la realidad y como fin; o es contingente el que se elija el medio que expresa el fin. Finalmente, reunidos estos momentos interiores, tengan en sí una unidad o no, el obrar del individuo es, a su vez, contingente con respecto a la realidad en general; la dicha decide tanto en pro de un fin mal determinado y de un medio mal escogido como en contra de ellos.

Ahora bien, si ahora, según esto, la conciencia ve ante sí, en su obra, la oposición entre la voluntad y la consumación, entre el fin y el medio y, a su vez, entre este interior conjunto y la realidad misma, lo que en general resume en sí el carácter contingente de su obrar se hallan igualmente presentes la unidad y la necesidad del obrar; este lado se entrelaza con aquél y la experiencia del carácter contingente del obrar sólo es, a su vez, una experiencia contingente. La necesidad del obrar consiste en que el fin sea referido simplemente a la realidad, y esta unidad es el concepto del obrar; se obra porque el obrar es en y para sí mismo la esencia de la realidad. Es cierto que en la obra se da como resultado la contingencia que el ser consumado tiene con respecto al querer y al consumar; y esta experiencia que parece debe valer como la verdad contradice a aquel concepto de la acción. Sin embargo, si consideramos en su integridad el contenido de esta experiencia, vemos que es la obra llamada a desaparecer; lo que se mantiene no es el desaparecer, sino que el desaparecer es, a su vez, real, se halla vinculado a la obra y desaparece a su vez con ella; lo negativo perece con lo positivo, cuya negación es."""
    },
    {
        "id": "r106",
        "pagina": 240,
        "texto": """Este desaparecer del desaparecer radica en el concepto mismo de la individualidad real en sí; pues aquello en que desaparece la obra o lo que en ella desaparece y lo que debería dar a lo que se llama experiencia su supremacía sobre el concepto que la individualidad tiene de sí misma es la realidad objetiva; pero ésta es un momento que tampoco en esta conciencia misma tiene ya ninguna verdad para sí; ésta consiste solamente en la unidad de la conciencia con el obrar, y la verdadera obra es solamente aquella unidad del obrar y del ser, del querer y del consumar. Por tanto, para la conciencia, en virtud de la certeza sobre que descansa su obrar, la realidad a ella contrapuesta es en sí misma una realidad tal que es solamente para ella; a la conciencia como autoconciencia retrotraída a sí misma y para la que ha desaparecido toda oposición, ésta no puede llegar a ser ya en esta forma de su ser para sí frente a la realidad; sino que la oposición y la negatividad que en la obra salen a luz afectan por ello no sólo al contenido de la obra o también al de la conciencia, sino a la realidad como tal y, por tanto, a la oposición presente solamente a través de aquélla y en ella y al desaparecer de la obra. De este modo, se refleja la conciencia en sí misma fuera de su obra perecedera y afirma su concepto y su certeza como lo que es y lo permanente frente a la experiencia del carácter contingente del obrar; la conciencia experimenta de hecho su concepto, en el que la realidad sólo es un momento, algo para ella, no en y para sí; experimenta la realidad como un momento llamado a desaparecer y que, por tanto, sólo vale para ella como ser en general, cuya universalidad es lo mismo que el obrar. Esta unidad es la obra verdadera; es la cosa misma que simplemente se afirma y se experimenta como lo permanente, independientemente de la cosa, que es lo contingente del obrar individual como tal, de las circunstancias, los medios y la realidad.

La cosa misma sólo aparece contrapuesta a estos momentos en la medida en que se los considera como aislados, pero es esencialmente la unidad de ellos, como compenetración de la realidad y la individualidad; la cosa misma es también, esencialmente, un obrar y, como tal, un puro obrar en general y, con ello, del mismo modo, un obrar de este individuo, este obrar que a él le pertenece en oposición con la realidad, como fin; y es asimismo el tránsito de esta determinabilidad a la contrapuesta y, por último, una realidad presente para la conciencia. La cosa misma expresa con ello la esencia..."""
    },
    {
        "id": "r107",
        "pagina": 241,
        "texto": """lidad espiritual en que todos estos momentos han sido superados como valederos para sí, en que, por tanto, sólo valían como elementos universales y en la que la certeza de sí misma es para la conciencia una esencia objetiva, una cosa [Sache], el objeto nacido de la autoconciencia como el suyo, sin dejar por ello de ser un objeto libre y auténtico. Ahora, la cosa [Ding] de la certeza sensible y de la percepción sólo tiene para la autoconciencia su significación a través de ésta; en esto descansa la diferencia entre una cosa [Ding] y una cosa [Sache]. Se desarrollará aquí un movimiento correspondiente al de la certeza sensible y la percepción.

Así, pues, en la cosa misma, como la compenetración objetivada de la individualidad y la objetividad misma deviene ante la autoconciencia su verdadero concepto de sí misma, o adquiere aquélla la conciencia de su sustancia. La autoconciencia es, al mismo tiempo, como es aquí, una conciencia que acaba de llegar a ser y que es, por tanto, una conciencia inmediata de la sustancia, siendo éste el modo determinado como se presenta aquí la esencia espiritual y que no ha llegado todavía a madurar como la sustancia verdaderamente real. La cosa misma tiene, en esta conciencia inmediata de la sustancia, la forma de la esencia simple, que contiene en sí y a la que corresponden, como universal, todos sus diversos momentos, pero que es, a su vez, indiferente con respecto a ellos, como momentos determinados, y libre para sí y que vale como la esencia en tanto que es esta cosa misma libre, simple y abstracta. Los diversos momentos de la determinabilidad originaria o de la cosa de este individuo, de su fin, de los medios, del obrar mismo y de la realidad, son para esta conciencia, de una parte, momentos singulares que esta conciencia puede abandonar y superar por la cosa misma; pero, de otra parte, todos ellos tienen como esencia la cosa misma solamente de tal modo que ésta se encuentra como la universalidad abstracta de ella en cada uno de estos momentos y puede ser predicado suyo. Ella misma no es todavía el sujeto, sino que valen como el sujeto aquellos momentos porque caen del lado de la singularidad en general, mientras que la cosa misma sólo es, de momento, lo simplemente universal. La cosa misma es el género, que se encuentra en todos estos momentos como en sus especies y que, al mismo tiempo, es libre de ellos.

[3. El mutuo engaño y la sustancia espiritual]

Se llama honrada la conciencia que, de una parte, ha llegado a este idealismo que la cosa misma expresa y que, de otra parte, tiene en..."""
    },
    {
        "id": "r108",
        "pagina": 242,
        "texto": """ella, como esta universalidad formal, lo verdadero; la que sólo se preocupa de la cosa misma y se mueve y afana, por tanto, en sus diversos momentos o especies, de tal modo que, cuando no encuentre la cosa misma en uno de ellos o en su significación, la encuentra precisamente por ello en el otro y, de este modo, alcanza siempre, de hecho, la satisfacción que esta conciencia debe lograr, con arreglo a su concepto. Ocurra lo que ocurra, esta conciencia consuma y alcanza la cosa misma, pues es, como este género universal de aquellos momentos, predicado de todos.

Si no lleva un fin a realidad, lo ha querido, sin embargo; es decir, hace del fin como fin, del puro obrar que no obra nada, la cosa misma, pudiendo por tanto decir, para consolarse, que, a pesar de todo, ha obrado e impulsado algo. Como lo universal contiene en sí mismo lo negativo o lo que tiende a desaparecer, también esto, el hecho de que la obra se anule es también su propio obrar; ha incitado a los otros a esto y encuentra todavía una satisfacción en la desaparición de su realidad, a la manera como los chicos traviesos gozan de sí mismos en la bofetada que reciben, a saber, como causa de ella. O bien, si la conciencia no ha intentado siquiera llevar a cabo la cosa misma ni ha obrado absolutamente nada, es porque no ha podido; la cosa misma, es, para ella, precisamente la unidad de su decisión y de la realidad; afirma que la realidad no sería sino lo posible para ella. Por último, si ha llegado a ser algo interesante para ella, en general, sin su concurso, esta realidad será para la conciencia la cosa misma precisamente por el interés que en ella encuentra, aunque no haya sido producida por ella; si es una dicha que personalmente obtiene, se atiene a ella como a un obrar y a un mérito suyos; y si se trata de un suceso del mundo que de otro modo no le atañe, lo hace también suyo y el interés parvio es para ella el partido que en pro o en contra adopta y que ha apoyado o combatido."""
    },
    {
        "id": "r109",
        "pagina": 243,
        "texto": """La honradez de esta conciencia y la satisfacción que encuentra en todos los casos consisten de hecho, como claramente se ve, en que no reúne y agrupa sus pensamientos, los pensamientos que tiene de la cosa misma. La cosa misma es, para ella, tanto su cosa como la ausencia total de obrar, o bien el puro obrar y el fin vacío, o también una realidad inactiva; esta conciencia hace de una significación tras otra el sujeto de este predicado y va olvidándolas a una tras otra. Ahora, en el mero haber querido o también en el no haber podido tiene la cosa misma la significación del fin vacío y de la unidad pensada del querer y el consumar. El consuelo de la anulación del fin que consiste en haber querido, sin embargo, algo o en haber obrado puramente, así como la satisfacción de haber dado algo que obrar a los otros, hace del puro obrar o de un obrar totalmente malo la esencia; pues lo que debe llamarse malo es el obrar que no es obrar alguno. Finalmente, en el caso afortunado de que encuentre la realidad, se convertirá este ser sin obrar en la cosa misma.

La verdad de esta honradez consiste, sin embargo, en no ser tan honrada como parece. En efecto, no puede ser tan carente de pensamiento que deje, de hecho, que estos diversos momentos se distinguen así, sino que tiene necesariamente que tener la conciencia inmediata de su oposición, sencillamente porque se refieren los unos a los otros. El puro obrar es esencialmente obrar de este individuo, y este obrar es no menos esencialmente una realidad o una cosa. Y, a la inversa, la realidad sólo es esencial como su obrar y también como el obrar en general; y así es también realidad. Por tanto, cuando al individuo le parece que sólo se trata de la cosa misma como realidad abstracta se halla presente el hecho de que se trata de ella como de su propio obrar. Y, del mismo modo, cuando cree que sólo se trata del obrar y del afanarse, no toma en serio esto, sino que se trata de una cosa y de la cosa como la suya. Finalmente, cuando parece querer solamente una cosa y su obrar, se trata, a su vez, de la cosa en general o de la realidad que permanece en y para sí.

Del mismo modo que la cosa misma y sus momentos se manifiestan aquí como contenido, igualmente necesarios son también como formas en la conciencia. Sólo surgen como contenido para desaparecer, y cada uno de ellos deja sitio al otro. Deben, por tanto, hallarse presentes en la determinabilidad, como momentos supuestos; pero así son lados de la conciencia misma. La cosa misma está presente como el en sí o su reflexión en sí misma; pero el desplazamiento de unos momentos por otros se expresa en la conciencia de tal modo que dichos momentos no se ponen en sí, sino que son puestos en ella solamente para un otro. Uno de los momentos del contenido es sacado a la luz del día por la conciencia y representado para otro; pero la conciencia, al mismo tiempo, se refleja fuera de ello en sí y lo contrapuesto se halla asimismo presente en ella; la conciencia lo retiene para sí como lo suyo. A la vez, no hay tampoco uno cualquiera de dichos momentos que se limite solamente a proyectarse hacia el exterior, mientras que otro es retenido solamente en lo interior, sino que la conciencia los mueve alternativamente, pues tiene que hacer tanto del uno como del otro algo esencial para sí y para los demás. El todo es la compenetración en movimiento de la individualidad y de lo universal, pero, como este todo sólo se halla presente para esta conciencia como la esencia simple, como la abstracción de la cosa misma, sus momentos caen fuera de ésta como momentos separados, disgregados unos de otros; y sólo se agotan y presentan como todo mediante la alternación separadora que los expone y los retiene para sí."""
    },
    {
        "id": "r110",
        "pagina": 244,
        "texto": """Ahora bien, como en este alternar la conciencia tiene a un momento para sí y como esencial en su reflexión y otro sólo exteriormente en ella o para los otros, aparece así un juego de las individualidades, unas con respecto a otras, en el que se engañan y son engañadas las unas por las otras, del mismo modo que se engañan a ellas mismas.

Una individualidad se dispone, pues, a llevar a cabo algo; parece, así, como si convirtiese algo en cosa; la individualidad obra, deviene en el obrar para otro y parece como si para ella se tratase aquí de la realidad. Los otros toman, por tanto, el obrar de aquélla por un interés en la cosa como tal y por fin, consistente en que la cosa en sí se lleve a cabo, siendo indiferente que lo haga la primera individualidad o lo hagan ellos. Cuando, según esto, muestran esta cosa como llevada ya a cabo por ellos o, si no, brindan y prestan su ayuda, aquella conciencia ha salido ya más bien de donde ellos suponen que está, es su obrar y afanarse lo que en la cosa interesa y, al percatarse de que esto era la cosa mismo, se consideran, por tanto, engañados. Pero, de hecho, su apresurarse para ayudar no era en sí mismo sino que ellos querían ver y mostrar su obrar, y no la cosa misma; es decir, querían engañar a los otros cabalmente del mismo modo que ellos se quejan de haber sido engañados. Y al ponerse de manifiesto, ahora, que el propio obrar y afanarse, el juego de sus fuerzas, vale como la cosa misma, parece como si la conciencia impulsara su esencia para sí y no para los otros y sólo se preocupara del obrar como el suyo y no como un obrar de los otros, dejando a éstos, así, hacer con respecto a la cosa de ellos. Pero, de nuevo se equivocan; la conciencia ya no está allí donde ellos suponen que está. La conciencia no se ocupa de la cosa como de esta su cosa singular, sino que se ocupa de ella como cosa, como universal, que es para todos. Se inmiscuye, por tanto, en su obrar y en su obra, y si no puede quitárselo de las manos, por lo menos se interesa por ello, preocupándose de emitir juicios; si le imprime el sello de su aprobación y de su elogio, quiere decir con ello que no se limita a elogiar en la obra la obra misma, sino que elogia al mismo tiempo su propia magnanimidad y moderación, al no echar a perder la obra como obra, ni tampoco con su censura. Y, al mostrar un interés por la obra, se goza a sí mismo en ello; y también la obra censurada por él le es grata precisamente por este goce de su propio obrar, goce que con ello se le procura. Y quienes se consideran o presentan como engañados por esta ingerencia trataban más bien ellos mismos de engañar del mismo modo. Tratan de hacer pasar su obrar y su afanarse por algo que sólo es para ellos mismos, en que no tienen otro fin que ellos mismos y su propia esencia. Pero, al hacer algo y presentarse y mostrarse así a la luz del día, contradicen de un modo inmediato con sus actos lo que dicen proponerse, el querer excluir la misma luz del día, la conciencia universal y la participación de todos; la realización es, por el contrario, una exposición de lo suyo en el elemento universal por medio del cual lo suyo se convierte y debe convertirse en cosa de todos."""
    },
    {
        "id": "r111",
        "pagina": 245,
        "texto": """Es también engañarse a sí mismo y engañar a los otros el pretender que se trata solamente de la pura cosa; una conciencia que pone de manifiesto una cosa hace más bien la experiencia de que los otros acuden volando como las moscas a la leche que se acaba de poner sobre la mesa y que quieren saberse ocupados en ello; pero éstos, por su parte, hacen en esa conciencia también la experiencia de que tampoco ella se ocupa de la cosa como objeto, sino como de la cosa suya. Por el contrario, si lo que debe ser lo esencial es solamente el obrar mismo, el uso de las fuerzas y capacidades o la expresión de esta individualidad, por ambas partes se hace asimismo la experiencia de que todos se agitan y se tienen por invitados y de que, en vez de un puro obrar o de un obrar singular y peculiar, se pone de manifiesto más bien algo que es igualmente para otros o una cosa misma. En ambos casos sucede lo mismo y sólo tiene un sentido distinto frente al que se había admitido y se consideraba que debía valer. La conciencia experimenta ambos lados como momentos igualmente esenciales y, en ello, la experiencia de lo que es la naturaleza de la cosa misma, a saber, que no es solamente cosa contrapuesta al obrar en general y al obrar singular, ni obrar que se contrapone a la subsistencia y que sería el género libre de estos momentos como sus especies, sino una esencia cuyo ser es el obrar del individuo singular y de todos los individuos y cuyo obrar es de un modo inmediato para otros o una cosa, que es cosa solamente como obrar de todos y de cada uno; la esencia que es la esencia de todas las esencias, la esencia espiritual. La conciencia experimenta que ninguno de aquellos momentos es sujeto, sino que se disuelve más bien en la cosa universal misma; los momentos de la individualidad, que para la carencia de pensamiento de esta conciencia valían uno tras otro como sujeto, se agrupan en la individualidad simple, que, al ser ésta, es al mismo tiempo inmediatamente universal. La cosa misma pierde, con ello, la relación de predicado y la determinabilidad de lo universal abstracto y sin vida, y es más bien la sustancia penetrada por la individualidad; el sujeto, en el que la individualidad es tanto como ella misma o como ésta así como todos los individuos, y lo universal que sólo es un ser como este obrar de todos y cada uno, una realidad por cuanto que esta conciencia la sabe como su realidad singular y como la realidad de todos. La pura cosa misma es lo que más arriba se determinaba como la categoría, el ser que es yo o el yo que es ser, pero como pensamiento que se distingue todavía de la autoconciencia real; pero, aquí los momentos de la autoconciencia real, en tanto que nosotros los llamamos su contenido, su fin, su obrar y su realidad, así como en tanto que los llamamos su forma, ser para sí y ser para otro, se ponen como unidad con la categoría simple misma, la cual es, así, al mismo tiempo, todo contenido."""
    },
    {
        "id": "r112",
        "pagina": 246,
        "texto": """b. LA RAZÓN LEGISLADORA

La esencia espiritual es, en su ser simple, pura conciencia, y ésta autoconciencia. La naturaleza originariamente determinada del individuo ha perdido su significación positiva de ser en sí el elemento y el fin de su actividad; es solamente un momento superado, y el individuo un sí mismo, como sí mismo universal. Y, a la inversa, la cosa formal misma tiene su cumplimiento en la individualidad que obra y se diferencia en sí misma; pues las diferencias de ésta constituyen el contenido de aquel universal. La categoría es en sí, como lo universal de la pura conciencia; y es asimismo para sí, pues el sí mismo de la conciencia es también su momento. La categoría es ser absoluto, pues aquella universalidad es la simple igualdad consigo mismo del ser.

Lo que, por tanto, es el objeto para la conciencia tiene la significación de ser lo verdadero; lo verdadero es y vale en el sentido de ser y de valer en y para sí mismo; es la cosa absoluta que no padece ya de la oposición entre la certeza y su verdad, entre lo universal y lo individual, entre el fin y su realidad [Realitat], sino que su ser allí es la realidad y el obrar de la autoconciencia; esta cosa es, por tanto, la sustancia ética, y la conciencia de ella la conciencia ética. Su objeto vale para esta conciencia, asimismo, como lo verdadero, pues agrupa en unidad autoconciencia y ser; vale como lo absoluto, pues la autoconciencia ya no puede ni quiere ir más allá de este objeto, ya que en él es cerca de sí misma: no puede, porque ese objeto es todo ser y todo poder, y no quiere, porque es el sí mismo o..."""
    },
    {
        "id": "r113",
        "pagina": 246,
        "texto": """la voluntad de este sí mismo. Es el objeto real [reales] en él mismo como objeto, pues tiene en él la diferencia de la conciencia; se divide en masas que son las leyes determinadas de la esencia absoluta. Pero estas masas no empañan el concepto, pues en éste permanecen incluidos los momentos del ser y de la conciencia pura y del sí mismo —una unidad que constituye la esencia de estas masas y que en esta diferencia no deja ya que estos momentos se separen.

Estas leyes o masas de la sustancia ética son reconocidas de un modo inmediato; no cabe preguntar por su origen y su justificación, ni indagar tampoco un otro cualquiera, ya que un otro que no fuese la esencia que es en y para sí sería solamente la autoconciencia misma; pero ésta no es otra cosa que esta esencia, pues ella misma es el ser para sí de esta esencia, que es cabalmente la verdad porque es tanto el sí mismo de la conciencia como su en sí o pura conciencia.

Por cuanto que la autoconciencia se sabe como momento del ser para sí de esta sustancia, expresa en ella el ser allí de la ley, de tal modo que la sana razón sabe de un modo inmediato lo que es justo y bueno. Y tan inmediatamente como lo sabe, tan inmediatamente vale para ella y puede decir, también de un modo inmediato: esto es bueno y justo. Y precisamente esto; se trata de leyes determinadas, de la cosa misma cumplida y plena de contenido.

Y lo que así se ofrece de un modo inmediato debe también acogerse y considerarse de modo inmediato; así como de aquello que la certeza sensible enuncia de un modo inmediato como lo que es hay que ver cómo está constituido, así también aquí hay que ver cómo está constituido el ser enunciado por esta certeza ética inmediata o cómo lo están estas masas de la esencia ética que son de un modo inmediato. Los ejemplos de algunas de tales leyes mostrarán esto, y al tomarlas bajo la forma de máximas de la sana razón dotada de saber no tendremos nosotros por qué empezar introduciendo el momento que hay que hacer valer en ellas, como leyes éticas inmediatas.

'Cada cual debe decir la verdad'. En este deber, enunciado como incondicionado, se admitirá en seguida una condición: si sabe la verdad. Por donde el precepto rezará, ahora, así: cada cual debe decir la verdad, siempre con arreglo a su conocimiento y a su convicción acerca de ella. La sana razón, precisamente esta conciencia ética que sabe de un modo inmediato lo que es justo y bueno, explicará también que esta condición se hallaba ya unida de tal modo a su máxima universal, que, al enunciar dicho precepto, lo suponía ya así. Con lo cual reconoce, de hecho, que, al enunciar la máxima, la infringe ya de un modo inmediato; decía que cada cual debe decir la verdad; pero suponía que debe decirla con arreglo a su conocimiento y a su convicción acerca de ella; en otros términos, decía otra cosa de lo que suponía; y decir otra cosa de lo que se supone significa no decir la verdad."""
    },
    {
        "id": "r114",
        "pagina": 247,
        "texto": """Una vez corregida la novedad o la torpeza, la máxima se enunciará así: cada cual debe decir la verdad, con arreglo al conocimiento y a la convicción que de ella tenga en cada caso. Pero, con ello, lo universal necesario, lo valedero en sí, que esta máxima se proponía enunciar, más bien se invierte, convirtiéndose en algo totalmente contingente. En efecto, el que se diga la verdad queda confiado al hecho contingente de que yo la conozca y pueda convencerme de ella; lo que vale tanto como afirmar que debe decirse lo verdadero y lo falso mezclado y revuelto, tal como uno lo conoce, lo supone y lo concibe. Esta contingencia del contenido sólo tiene la universalidad en la forma de una proposición bajo la cual se expresa; pero, como máxima ética promete un contenido universal y necesario y se contradice a sí misma, con la contingencia de dicho contenido. Y si, por último, la máxima se corrige diciendo que la contingencia del conocimiento y de la convicción acerca de la verdad deben desaparecer y que la verdad debe, además, ser sabida, se enunciará con ello un precepto en flagrante contradicción con lo que era el punto de que se partía. Primeramente, la sana razón debía tener de un modo inmediato la capacidad de enunciar la verdad; pero ahora se dice que debía saber la verdad, es decir, que no sabe enunciarla de un modo inmediato. Considerando el problema por el lado del contenido, éste se descarta al exigir que se debe saber la verdad, ya que esta exigencia se refiere al saber en general: se debe saber; lo que se exige es, por tanto, más bien lo que se halla libre de todo contenido determinado. Pero aquí se hablaba de un contenido determinado, de una diferencia en cuanto a la sustancia ética. Sin embargo, esta determinación inmediata de dicha sustancia es un contenido que se manifiesta más bien como algo totalmente fortuito y que se eleva a universalidad y necesidad, de tal modo que más bien desaparece el saber enunciado como ley."""
    },
    {
        "id": "r115",
        "pagina": 248,
        "texto": """Otro precepto famoso es el de 'ama a tu prójimo como a ti mismo'. Es un precepto dirigido al individuo en relación con otros individuos, en que se afirma como una relación entre individuo e individuo, o como relación de sentimiento. El amor activo —pues el inactivo no tiene ser alguno y, evidentemente, no puede tratarse de él— tiende a evitar el mal a un ser humano y a hacerle el bien. A este efecto, hay que distinguir lo que para él es el mal, lo que es frente a éste el bien eficiente y lo que es, en general, su bienestar; es decir, que debemos amar al prójimo de un modo inteligente, pues un amor no inteligente le hará tal vez más daño que el odio. Ahora bien, el obrar bien de un modo esencial e inteligente es, en su figura más rica y más importante, la acción inteligente universal del Estado —una acción en comparación con la cual el obrar del individuo como individuo es, en general, algo tan insignificante, que apenas si vale la pena de hablar de ello. Además, aquella acción es tan poderosa, que si oponemos a ella el obrar individual y éste quisiera ser precisamente para sí un delito o defraudar por amor a otro lo universal en lo tocante al derecho y a la participación que tiene en él, ese obrar individual resultaría totalmente estéril y sería irresistiblemente destruido. A ese bien obrar que es sentimiento sólo le resta la significación de un obrar totalmente individual, de una ayuda en caso extremo, que será algo tan contingente como momentáneo. Lo fortuito determina no sólo su ocasión, sino también el si es o no, en general, una obra, el si esta obra no vuelve a disolverse en seguida y se convierte por sí misma más bien en un mal. Por tanto, este obrar en bien de otros que se enuncia como necesario es de tal naturaleza, que podría tal vez existir y tal vez no; que, el caso se ofrece fortuitamente, es tal vez una obra, es tal vez una obra buena o tal vez no. Así, pues, esta ley carece de un contenido universal, ni más ni menos que la primera que ha sido considerada, y no expresa algo que sea en y para sí, como tendría que hacerlo en tanto que ley ética absoluta. O bien tales leyes se mantienen en el terreno del deber ser, pero carecen de realidad y no son leyes, sino solamente preceptos."""
    },
    {
        "id": "r116",
        "pagina": 249,
        "texto": """Pero, de hecho, se ve claramente por la naturaleza de la cosa misma que es necesario renunciar a un contenido universal y absoluto; pues a la sustancia simple, cuya esencia consiste en ser sustancia simple, es inadecuada toda determinabilidad que en ella se ponga. El precepto, en su absolutidad simple, enuncia por sí mismo un ser ético inmediato; la diferencia que en él se manifiesta es una determinabilidad, y por tanto un contenido, que se halla bajo la universalidad absoluta de este ser simple. Y, teniendo, según esto, que renunciar a un contenido absoluto, sólo puede asignarse al precepto una universalidad formal, o sea el que no se contradiga, pues la universalidad carente de contenido es la universalidad formal, y un contenido absoluto significa él mismo tanto, a su vez, como una diferencia que no es tal o como la carencia de contenido.

Lo que resta, por tanto, para la razón legisladora es la pura forma de la universalidad o, de hecho, la tautología de la conciencia, tautología que se contrapone al contenido y que es un saber, no del contenido que es o del contenido propiamente dicho, sino de la esencia o de la igualdad de ese contenido consigo mismo.

Así, pues, la esencia ética no es ella misma e inmediatamente un contenido, sino solamente una pauta para medir si un contenido es capaz de ser o no ley, en cuanto que no se contradice a sí mismo. La razón legisladora desciende, así, al plano de una razón simplemente examinadora."""
    },
    {
        "id": "r117",
        "pagina": 250,
        "texto": """c. LA RAZÓN QUE EXAMINA LEYES

Una diferencia en la sustancia ética simple es para ella algo fortuito que en el precepto determinado hemos visto surgir como algo fortuito del saber, de la realidad y del obrar. La comparación entre aquel ser simple y la determinabilidad que no corresponde a él recaía en nosotros; y la sustancia simple se ha mostrado ser universalidad formal o pura conciencia que, libre del contenido, se enfrenta a él y es un saber de él como contenido determinado. Esta universalidad sigue siendo, de este modo, lo que era, propiamente, la cosa misma. Pero es, en la conciencia, algo otro; no es ya, en efecto, el género inerte y carente de pensamiento, sino que se refiere a lo particular y vale como la potencia y la verdad de esto. Esta conciencia parece ser, primeramente, el mismo examinar que antes éramos nosotros mismos, y su acción no parece que pueda ser otra de lo que antes acaeció, a saber, una comparación entre lo universal y lo determinado, de la que resultaría, como antes, su inadecuación. Pero la relación entre el contenido y lo universal es aquí otra, ya que lo universal ha cobrado aquí otra significación; ahora, es una universalidad formal, de la que es capaz el contenido determinado, pues en ella éste es considerado solamente en relación consigo mismo. En nuestro examen, la sustancia universal sólida se enfrentaba a la determinabilidad que se desarrollaba como lo fortuito de la conciencia en que entraba la sustancia. Aquí, en cambio, ha desaparecido uno de los términos de la comparación; lo universal no es ya la sustancia que es y que vale o lo justo en y para sí, sino simple saber o forma que compara un contenido solamente consigo mismo y lo considera para saber si es una tautología. Aquí, ya no se estatuyen leyes, sino que solamente se examinan; y las leyes están ya dadas para la conciencia examinadora; ésta acoge su contenido tal y como es simplemente, sin entrar en la consideración de lo singular y lo fortuito adherido a su realidad, como nosotros hacíamos, sino que se detiene en el precepto como tal precepto y se comporta con respecto a él de un modo igualmente simple, como lo que es simplemente su pauta."""
    },
    {
        "id": "r118",
        "pagina": 250,
        "texto": """Pero, por esta misma razón, este examen no va muy lejos; cabalmente por cuanto que la pauta es la tautología y es indiferente hacia el contenido, acoge en sí lo mismo éste que el contrapuesto. Si se pregunta si debe ser una ley en y para sí el que exista propiedad; en y para sí, no por razones de utilidad para otros fines; la esencialidad ética consiste precisamente en que la ley sea solamente igual a sí misma y, por medio de esta igualdad consigo misma, se halle fundada, por tanto, en su propia esencia, y no sea algo condicionado. La propiedad en y para sí no se contradice; es una determinabilidad aislada o una determinabilidad que se pone sólo como igual a sí misma. Del mismo modo que no se contradice tampoco la no-propiedad, la ausencia de propietario de las cosas o la comunidad de bienes. El que algo no pertenezca a nadie, o pertenezca al primero que llegue y se posesione de ello, o pertenezca a todos y a cada uno según sus necesidades o por partes iguales, es una determinabilidad simple, un pensamiento formal, como su contrario, la propiedad. Claro está que si la cosa sin dueño es considerada como un objeto necesario para la satisfacción de una necesidad, será necesario que se convierta en posesión de un individuo cualquiera; y sería contradictorio convertir más bien en ley la libertad de la cosa. Pero por carencia de dueño de la cosa no se supone tampoco una ausencia absoluta de dueño, sino que la cosa deberá convertirse en posesión con arreglo a la necesidad del individuo, y no precisamente para ser guardada, sino para usarla inmediatamente. Pero el velar así por las necesidades, ateniéndose exclusivamente a lo fortuito, es contradictorio con la naturaleza de la esencia consciente, que es la única de que se habla; pues ésta tiene necesariamente que representarse sus necesidades en la forma de universalidad, velar por toda su existencia y adquirir un bien permanente. Por donde no coincidiría consigo mismo el pensamiento de que se atribuyese fortuitamente la posesión de una cosa a la primera vida autoconsciente que se presentara, con arreglo a sus necesidades. En la comunidad de bienes en que se velase por ello de un modo universal y permanente se darían dos posibilidades, o bien se asignaría a cada uno tanto como necesitara, en cuyo caso se hallarían en contradicción esta desigualdad y la esencia de la conciencia, para la que la igualdad de los individuos es un principio. O bien, con arreglo a este último principio, la distribución se basará en la igualdad, y en este caso la participación no guardaría ya relación con la necesidad, que es, sin embargo, la única que constituye su concepto.

Pero, si de este modo la no-propiedad se manifiesta como contradictoria es solamente porque no se la ha dejado como determinabilidad simple."""
    },
    {
        "id": "r119",
        "pagina": 251,
        "texto": """Lo mismo ocurre con la propiedad cuando se la disuelve en momentos. La cosa singular que es mi propiedad vale, así, como algo universal, firme y permanente; pero esto contradice a su naturaleza, que consiste en ser usada y desaparecer. Y vale, al mismo tiempo, como lo mío, que todos los demás reconocen y de lo que se excluyen. Ahora bien, el hecho de que se me reconozca radica más bien en mi igualdad con todos, en lo contrario de la exclusión. Lo que yo poseo es una cosa, es decir, un ser para otros en general, de modo totalmente universal y sin la determinación de ser solamente para mí; el que yo la posea contradice a su sociedad universal. Por tanto, la propiedad se contradice por todos sus lados ni más ni menos que la no-propiedad; tanto una como otra llevan en sí estos dos momentos contrapuestos y contradictorios de la singularidad y la universalidad. Pero cada una de estas determinabilidades, representada como algo simple, como propiedad o como no-propiedad sin más desarrollo, es tan simple como la otra, es decir, no se contradice. Por tanto, la pauta de la ley, que la razón tiene en ella misma, conviene igualmente a todas y no es, según esto, de hecho, ninguna pauta. Sería, ciertamente, algo bien extraño que la tautología, el principio de contradicción, que para el conocimiento de la verdad teórica se reconoce solamente como un criterio formal, es decir, como algo totalmente indiferente hacia la verdad y la no-verdad, debiera ser algo más que esto con respecto al conocimiento de la verdad práctica."""
    },
    {
        "id": "r120",
        "pagina": 252,
        "texto": """En los dos momentos que acabamos de considerar, en los que se cumple una esencia espiritual antes vacía, se han superado el poner determinabilidades inmediatas en la sustancia ética y después el saber de ellas si son o no leyes. Por donde parece llegarse al resultado de que no hay lugar ni para leyes determinadas ni para un saber de ellas. Sin embargo, la sustancia es la conciencia de sí como esencialidad absoluta, que, así, no puede rechazar ni la diferencia presente en ella ni el saber de ella. El que el legislar y el examinar leyes hayan demostrado no ser nada, significa que los dos procesos, considerados cada uno de por sí y aisladamente, son solamente momentos inestables de la conciencia ética; y el movimiento en el que surgen tiene el sentido formal de que la sustancia ética se presenta a través de él como conciencia.

En tanto que estos dos momentos son determinaciones más precisas de la conciencia de la cosa misma, pueden ser considerados como formas de la honestidad, la cual, como en otros casos se ocupa de sus momentos formales, se afana aquí con un contenido, que debiera ser, de lo bueno y de lo justo y con un examen de esta verdad firme, creyendo poseer en la sana razón y en el discernimiento inteligente la fuerza y la validez de preceptos."""
    },
    {
        "id": "r121",
        "pagina": 253,
        "texto": """Pero, sin esta honestidad, las leyes no valen como esencia de la conciencia, ni el examen de ellas vale tampoco como un obrar dentro de ésta; sino que estos momentos, cuando surgen cada uno para sí, de modo inmediato y como una realidad, expresan uno un estatuir y un ser no valederos de leyes reales y el otro la liberación igualmente no valedera de esas leyes. La ley tiene, como ley determinada, un contenido fortuito —lo que significa, aquí, que es ley de una conciencia singular con un contenido arbitrario. Ese inmediato legislar es, por tanto, la temeridad tiránica que convierte la arbitrariedad en ley y la eticidad en una obediencia a ésta —a leyes que son solamente leyes, pero, que no son, a la vez, preceptos. Del mismo modo que el segundo momento, en tanto que aislado, el examen de las leyes significa el movimiento de lo inmóvil y la temeridad del saber que se libera de las leyes absolutas por medio del raciocinio y las considera como una arbitrariedad extraña a él.

En ambas formas son estos momentos un comportamiento negativo ante la sustancia o ante la esencia espiritual real [reales]; en otras palabras, la sustancia no tiene todavía en ellas su realidad [Realidad], sino que la conciencia los contiene todavía bajo la forma de su propia inmediatez, y la sustancia es solamente un querer y un saber de este individuo o el deber ser de un precepto no-real y un saber de la universalidad formal. Pero, al superarse estos modos, la conciencia ha retomado a lo universal y aquellas oposiciones han desaparecido. La esencia espiritual es sustancia real por el hecho de que estos modos no tienen validez en su singularidad, sino solamente como modos superados; y la unidad en la que son solamente momentos es el mismo de la conciencia, que, puesto de ahora en adelante en la esencia espiritual, eleva ésta a lo real, lo pleno y lo autoconsciente.

La esencia espiritual es, según esto, en primer lugar, para la autoconciencia como ley que es en sí; la universalidad del examen, que era universalidad formal que no era en sí, se ha superado. Y es en segundo lugar, una ley eterna, que no tiene su fundamento en la voluntad de este individuo, sino que es en y para sí, la absoluta voluntad pura de todos, que tiene la forma del ser inmediato. Este puro querer no es tampoco un precepto que solamente deba ser, sino que es y vale; es el yo universal de la categoría, que es de un modo inmediato la realidad, y el mundo es solamente esta realidad. Pero, por cuanto que esta ley que es vale sin más, la obediencia de la autoconciencia no es el servicio a un señor cuyas órdenes sean una arbitrariedad y en que la autoconciencia no se reconozca. Antes bien, las leyes son pensamientos de su propia conciencia absoluta, pensamientos que ella misma tiene de un modo inmediato. Y no se trata tampoco de que crea en ellos, pues si la fe puede intuir la esencia, es una esencia extraña. La autoconciencia ética forma unidad inmediata con la esencia por medio de la universalidad de su Sí mismo; la fe, por el contrario, parte de la conciencia singular, es el movimiento de esta conciencia que tiende siempre a acercarse a dicha unidad, sin alcanzar la presencia de su esencia. Por el contrario, aquella conciencia se ha superado como singular, esta mediación se ha llevado a cabo y sólo por haber sido llevada a cabo es autoconciencia inmediata de la sustancia ética."""
    },
    {
        "id": "r122",
        "pagina": 254,
        "texto": """La diferencia entre la autoconciencia y la esencia es, pues, perfectamente transparente. Esto hace que las diferencias en la esencia misma no sean determinaciones fortuitas, sino que, en virtud de la unidad de la esencia y de la autoconciencia única, de la que podría provenir la desigualdad, dichas diferencias son las masas en las que la unidad se estructura, infundiéndoles su propia vida, espíritus no desdoblados y claros ante sí mismos, figuras celestiales inmaculadas que conservan en sus diferencias la inocencia virginal y la armonía de su esencia. La autoconciencia es, asimismo, un comportamiento simple y claro hacia ellas. Son, y nada más: esto es lo que constituye la conciencia de su relación. Por eso estas leyes valen para la Antígona de Sófocles como el derecho no escrito e infalible de los dioses.

'No de hoy ni de ayer, sino de siempre
Este derecho vive, y nadie sabe de dónde ha aparecido.'*

Son. Si inquiero su nacimiento y las circunscribo al punto de su origen, voy ya más allá de ellas; pues yo soy de ahora en adelante lo universal y ellas son lo condicionado y lo limitado. Y si tienen que legitimarse ante mi modo de ver, es que ya he movido su inconmovible ser en sí y las considero como algo que para mí tal vez es verdadero y tal vez no. La disposición ética consiste precisamente en atenerse firme e inconmoviblemente a lo que es lo justo, absteniéndose de todo lo que sea moverlo, removerlo y derivarlo. Se me hace depositario de algo que es propiedad de otro, y yo lo reconozco porque es así, y me mantengo inconmovible en esta actitud. Pero si retengo el depósito para mí, no incurro para nada, según el principio de mi examen, de la tautología, en una contradicción; pues entonces ya no lo considero como propiedad de otro; retener algo que no considero propiedad de otro es perfectamente consecuente. Cambiar de punto de vista no es una contradicción; en efecto, de lo que aquí se trata no es del punto de vista como tal, sino del objeto y del contenido, que no debe contradecirse. Lo mismo que —como hago cuando me desprendo de algo, regalándolo— puedo cambiar el punto de vista de que algo es mi propiedad por el punto de vista de que es propiedad de otro; sin incurrir con ello en contradicción, exactamente lo mismo puedo seguir el camino inverso."""
    },
    {
        "id": "r123",
        "pagina": 255,
        "texto": """Así, pues, no porque encuentre algo no contradictorio es esto justo, sino que es justo porque es lo justo. Que algo es propiedad de otro: he ahí el fundamento de que se parte; acerca de eso no tengo por qué razonar, no tengo para qué indagar ni dejar que se me ocurran tales o cuales pensamientos, conexiones o consideraciones, ni ponerme a estatuir leyes o a examinarlas; mediante tales movimientos de mi pensamiento no haría más que trastocar aquella actitud, ya que, de hecho, podría a mi antojo hacer que fuera también lo contrario de esto lo conforme a mi saber tautológico indeterminado, convirtiéndolo, por tanto, en ley. Sino que lo justo sea esta determinación o la contrapuesta se determina en y para sí; yo podría, para mí, erigir en ley la que quisiera o ninguna y, desde el momento en que comienzo a examinar, marcho ya por un camino no ético. Cuando lo justo es para mí en y para sí es cuando soy dentro de la sustancia ética; ésta es, así, la esencia de la autoconciencia; pero ésta es su realidad y su ser allí, su sí mismo y su voluntad.

* Sófocles, Antígona, vv. 456-457."""
    }
]

# Notas de análisis del Capítulo V
NOTAS_RAZON = {
    "r01": "Fragmento r01 (p143): Introducción a la razón; la conciencia retorna a sí misma; la certeza de ser toda verdad.",
    "r02": "Fragmento r02 (p143): La autoconciencia como razón; actitud positiva ante el mundo; la certeza de ser toda realidad.",
    "r03": "Fragmento r03 (p144): La razón como certeza inmediata; el idealismo; el camino olvidado.",
    "r04": "Fragmento r04 (p145): Crítica del idealismo abstracto; la certeza debe demostrarse.",
    "r05": "Fragmento r05 (p145-146): La categoría simple; la diferencia en la unidad; el mal idealismo.",
    "r06": "Fragmento r06 (p146-147): La multiplicidad de categorías; la negatividad y la singularidad.",
    "r07": "Fragmento r07 (p148): Inicio de la razón observante; retorno a la percepción con nueva certeza.",
    "r08": "Fragmento r08 (p148): La razón como instinto que busca su otro; la certeza no es aún verdad.",
    "r09": "Fragmento r09 (p149): El instinto de la razón es el observar; eleva el objeto a concepto.",
    "r10": "Fragmento r10 (p149): Inicio de la observación de la naturaleza; el concepto como algo encontrado.",
    "r11": "Fragmento r11 (p150): La observación busca la especie y la ley; la ley no es aún el concepto.",
    "r12": "Fragmento r12 (p151): La ley es un ser otro; la razón no se reconoce en ella.",
    "r13": "Fragmento r13 (p152): Las leyes de la naturaleza; la razón solo se encontrará en el espíritu.",
    "r14": "Fragmento r14 (p153): Inicio de la observación de lo orgánico; lo orgánico como fin en sí.",
    "r15": "Fragmento r15 (p154): Lo orgánico tiene doble forma: propiedades simples y figura.",
    "r16": "Fragmento r16 (p155): Intento de relacionar momentos del concepto con sistemas anatómicos; fracaso.",
    "r17": "Fragmento r17 (p156): Relación entre lo orgánico y lo inorgánico; leyes superficiales.",
    "r18": "Fragmento r18 (p157): El concepto de fin permanece oculto para la observación.",
    "r19": "Fragmento r19 (p158): Lo orgánico se conserva a sí mismo; la observación no reconoce el concepto.",
    "r20": "Fragmento r20 (p159): La autoconciencia se halla constituida como lo orgánico.",
    "r21": "Fragmento r21 (p160): La necesidad en lo orgánico como relación contingente.",
    "r22": "Fragmento r22 (p161): La unidad de universalidad y actividad no es para la observación.",
    "r23": "Fragmento r23 (p162): Lo externo como expresión de lo interno; la sustancia orgánica como alma simple.",
    "r24": "Fragmento r24 (p163): Las propiedades orgánicas simples: sensibilidad, irritabilidad, reproducción.",
    "r25": "Fragmento r25 (p164): La oposición cualitativa se vuelve cuantitativa; leyes tautológicas.",
    "r26": "Fragmento r26 (p165): Ejemplos de tautología; indiferencia de los opuestos.",
    "r27": "Fragmento r27 (p166): El juego vacío de la formulación de leyes.",
    "r28": "Fragmento r28 (p167): Los momentos del concepto descienden a propiedades comunes.",
    "r29": "Fragmento r29 (p168): Observaciones sobre diferencias de sensibilidad; no constituyen leyes.",
    "r30": "Fragmento r30 (p169): Comparación con sistemas anatómicos; la anatomía solo capta el cadáver.",
    "r31": "Fragmento r31 (p170): El ser del organismo es universalidad; los momentos son procesos.",
    "r32": "Fragmento r32 (p171): En lo orgánico se pierde la representación de la ley.",
    "r33": "Fragmento r33 (p172): Inicio de la observación de la autoconciencia.",
    "r34": "Fragmento r34 (p173): Las leyes lógicas son formas vacías; la psicología da generalizaciones empíricas.",
    "r35": "Fragmento r35 (p174): Fisiognómica y frenología; el extremo de la observación.",
    "r36": "Fragmento r36 (p175): Recorrido de la observación de la autoconciencia; paso a la razón práctica.",
    "r37": "Fragmento r37 (p176): Lo interno y lo externo son lo mismo en el movimiento.",
    "r38": "Fragmento r38 (p177): Crítica de la frenología como conclusión de la razón observante.",
    "r39": "Fragmento r39 (p178): La inversión grotesca en la frenología; el espíritu como hueso.",
    "r40": "Fragmento r40 (p179): Fin de la razón observante; paso a la razón práctica.",
    "r41": "Fragmento r41 (p180): Observación de la autoconciencia en su pureza; leyes lógicas y psicológicas.",
    "r42": "Fragmento r42 (p181): Crítica de las leyes lógicas como fijaciones del movimiento pensante.",
    "r43": "Fragmento r43 (p181-182): Introducción a las leyes psicológicas; la conciencia operante.",
    "r44": "Fragmento r44 (p182-183): La psicología como colección de facultades; crítica.",
    "r45": "Fragmento r45 (p183-184): La ley de la individualidad; relación con las circunstancias.",
    "r46": "Fragmento r46 (p184-185): La libertad del individuo frente a las circunstancias.",
    "r47": "Fragmento r47 (p186): La individualidad total; el cuerpo como expresión del interior.",
    "r48": "Fragmento r48 (p187): Lenguaje y trabajo como exteriorizaciones; su ambigüedad.",
    "r49": "Fragmento r49 (p187-188): La figura exterior como signo contingente; la fisiognómica.",
    "r50": "Fragmento r50 (p188-189): La mano como órgano activo; comparación con Solón.",
    "r51": "Fragmento r51 (p189-190): El término medio como exteriorización retrotraída; la multivocidad del signo.",
    "r52": "Fragmento r52 (p190-191): La individualidad pone su esencia en la obra; crítica de la fisiognómica.",
    "r53": "Fragmento r53 (p191-192): Las leyes de la fisiognómica son suposiciones vacías; cita de Lichtenberg.",
    "r54": "Fragmento r54 (p192): La obra como verdadera realidad; la figura no es el en sí.",
    "r55": "Fragmento r55 (p192-193): Transición a la frenología; el espíritu en su existencia fija.",
    "r56": "Fragmento r56 (p193): El cráneo como 'caput mortuum'; crítica del lenguaje inadecuado.",
    "r57": "Fragmento r57 (p193-194): Relación entre cerebro y cráneo; la influencia es subjetiva.",
    "r58": "Fragmento r58 (p194-195): La frenología como culminación y autodisolución de la observación.",
    "r59": "Fragmento r59 (p196): Conclusión de la razón observante; paso a la razón práctica.",
    "r60": "Fragmento r60 (p196-197): La relación causal indeterminada; armonía preestablecida.",
    "r61": "Fragmento r61 (p197-198): Indeterminación de la causa; ironía del emplasto.",
    "r62": "Fragmento r62 (p198-199): El cráneo no es órgano ni signo; es una cosa indiferente.",
    "r63": "Fragmento r63 (p199-200): La hipótesis de las sensaciones locales es infundada.",
    "r64": "Fragmento r64 (p200): La analogía con los granos de arena; arbitrariedad.",
    "r65": "Fragmento r65 (p200-201): La posibilidad vacía; la frenología natural.",
    "r66": "Fragmento r66 (p202-203): La disposición como excusa; la posibilidad vacía.",
    "r67": "Fragmento r67 (p203): El ser no es la verdad del espíritu; la réplica de la bofetada.",
    "r68": "Fragmento r68 (p203-204): El tosco instinto de la razón; analogía con el pueblo judío.",
    "r69": "Fragmento r69 (p204-205): Resumen de la observación; paso al espíritu.",
    "r70": "Fragmento r70 (p205-206): La observación retorna al ser fijo; el espíritu como hueso.",
    "r71": "Fragmento r71 (p206-207): Doble significación del resultado; la categoría y el juicio infinito.",
    "r72": "Fragmento r72 (p207-208): La analogía con el órgano urinario; la conciencia representativa.",
    "r73": "Fragmento r73 (p208): Inicio de la razón práctica; la autoconciencia ha encontrado la cosa como sí misma.",
    "r74": "Fragmento r74 (p208-209): Introducción al reino de la ética; la sustancia ética.",
    "r75": "Fragmento r75 (p209-210): La vida de un pueblo como realización de la razón; el trabajo universal.",
    "r76": "Fragmento r76 (p210-211): Las leyes como expresión de la individualidad; la máxima de los sabios antiguos.",
    "r77": "Fragmento r77 (p211-212): La necesaria salida de la dicha ética; el surgimiento de la singularidad.",
    "r78": "Fragmento r78 (p212-214): La autoconciencia abandona la sustancia ética; su fin es realizarse como singular.",
    "r79": "Fragmento r79 (p214): Inicio de 'El placer y la necesidad'; la autoconciencia se entrega al placer; cita de Goethe.",
    "r80": "Fragmento r80 (p214-215): El placer como acción de apetencia; la autoconciencia se supera.",
    "r81": "Fragmento r81 (p215-216): La necesidad como potencia negativa; la individualidad se estrella contra el destino.",
    "r82": "Fragmento r82 (p216-217): La contradicción en la autoconciencia; el tránsito de la vida a la muerte.",
    "r83": "Fragmento r83 (p217-218): Inicio de 'La ley del corazón'; la ley inmediata en el ser para sí.",
    "r84": "Fragmento r84 (p218-219): La ley del corazón como unidad inmediata de individualidad y necesidad.",
    "r85": "Fragmento r85 (p219-220): La realización de la ley del corazón la enajena; el individuo se enreda en un orden hostil.",
    "r86": "Fragmento r86 (p220-221): Los actos del individuo son particulares pero pretenden valer como universales.",
    "r87": "Fragmento r87 (p221-222): La conciencia desconoce la naturaleza de la realización; encuentra el orden animado.",
    "r88": "Fragmento r88 (p222): La rebelión de la individualidad; la conciencia como demencialidad.",
    "r89": "Fragmento r89 (p222-224): La furia de la infatuación demencial; el corazón se vuelve contra sí mismo.",
    "r90": "Fragmento r90 (p224-225): El orden universal como lucha de todos contra todos; el curso del mundo.",
    "r91": "Fragmento r91 (p225): Transición a la virtud; la virtud como sacrificio de la individualidad.",
    "r92": "Fragmento r92 (p225-226): Análisis del curso del mundo; sus momentos son el placer y la ley del corazón.",
    "r93": "Fragmento r93 (p226-227): La virtud cree en el bien en sí; las armas son los dones y capacidades.",
    "r94": "Fragmento r94 (p227-228): La lucha es imposible; la virtud no puede atacar al curso del mundo.",
    "r95": "Fragmento r95 (p228-229): El curso del mundo es la conciencia despierta; la virtud es derrotada.",
    "r96": "Fragmento r96 (p229-230): La virtud es vencida porque su fin es abstracto; crítica de la retórica vacía.",
    "r97": "Fragmento r97 (p230-231): La vacuidad de la retórica; el curso del mundo no es tan malo.",
    "r98": "Fragmento r98 (p231): Inicio de 'La individualidad real'; la autoconciencia capta que su obrar es fin en sí mismo.",
    "r99": "Fragmento r99 (p231-232): La autoconciencia tiene la categoría como objeto; el obrar como círculo.",
    "r100": "Fragmento r100 (p233): La individualidad como naturaleza originaria; analogía con la vida animal.",
    "r101": "Fragmento r101 (p234): El círculo del obrar; circunstancias, interés, talento.",
    "r102": "Fragmento r102 (p236): La obra introduce la diferencia; crítica de la comparación moral.",
    "r103": "Fragmento r103 (p237): El individuo se traduce de la noche de la posibilidad al día de la presencia.",
    "r104": "Fragmento r104 (p238-239): La obra es perecedera; el juego de fuerzas entre individualidades.",
    "r105": "Fragmento r105 (p239-240): La contradicción en la obra; la contingencia del fin y los medios.",
    "r106": "Fragmento r106 (p240-241): El desaparecer del desaparecer; la cosa misma como obra verdadera.",
    "r107": "Fragmento r107 (p241-242): Distinción entre Ding y Sache; la cosa misma como género.",
    "r108": "Fragmento r108 (p242-243): La conciencia honrada encuentra la cosa misma en cualquier circunstancia.",
    "r109": "Fragmento r109 (p243-244): La honradez es aparente; la conciencia alterna entre momentos sin síntesis.",
    "r110": "Fragmento r110 (p244-245): El mutuo engaño; las individualidades se engañan al pretender ocuparse de la cosa pura.",
    "r111": "Fragmento r111 (p245-246): La experiencia muestra que la cosa misma es la esencia espiritual.",
    "r112": "Fragmento r112 (p246): Inicio de la razón legisladora; la sustancia ética como objeto.",
    "r113": "Fragmento r113 (p246-247): La razón legisladora; crítica del precepto 'decir la verdad'.",
    "r114": "Fragmento r114 (p247-248): La contingencia del conocimiento destruye la universalidad.",
    "r115": "Fragmento r115 (p248-249): Crítica del precepto 'amar al prójimo'; el amor inteligente es obra del Estado.",
    "r116": "Fragmento r116 (p249-250): La sustancia ética no admite contenido determinado; reducción a tautología.",
    "r117": "Fragmento r117 (p250): Inicio de la razón examinadora; comparación formal.",
    "r118": "Fragmento r118 (p250-251): La propiedad y la no-propiedad son ambas no contradictorias.",
    "r119": "Fragmento r119 (p251-252): La propiedad se contradice al ser analizada; la tautología no es criterio.",
    "r120": "Fragmento r120 (p252): Los momentos de legislar y examinar se superan; la sustancia ética emerge.",
    "r121": "Fragmento r121 (p253-254): Sin honestidad, legislar es tiranía y examinar es raciocinio vacío.",
    "r122": "Fragmento r122 (p254-255): La ley ética es inmediata, como en Antígona; cambiar de punto de vista no es contradicción.",
    "r123": "Fragmento r123 (p255): Lo justo es justo porque es; tránsito al Espíritu."
}

# Ejemplos concretos del Capítulo V
EJEMPLOS_RAZON = {
    "r26": [{"tipo": "agujero", "descripcion": "La magnitud del agujero y lo que lo llena; tautología"}],
    "r27": [{"tipo": "brújula", "descripcion": "Los polos Norte y Sur tienen la misma fuerza"}],
    "r29": [{"tipo": "caballo", "descripcion": "Comportamiento diferente ante la cebada y el heno"}],
    "r50": [{"tipo": "Solón", "descripcion": "Conocer al hombre por el curso de toda su vida"}],
    "r53": [{"tipo": "Lichtenberg", "descripcion": "La bofetada como réplica al fisonomista"}],
    "r58": [{"tipo": "frenología", "descripcion": "El espíritu es un hueso"}],
    "r64": [{"tipo": "hijos de Israel", "descripcion": "Los granos de arena como símbolo"}],
    "r67": [{"tipo": "bofetada", "descripcion": "Réplica al frenólogo"}],
    "r72": [{"tipo": "órgano urinario", "descripcion": "La conciencia representativa se comporta como el orinar"}],
    "r79": [{"tipo": "Fausto", "descripcion": "Cita de Goethe: 'Desprecia al entendimiento y a la ciencia'"}],
    "r89": [{"tipo": "chicos traviesos", "descripcion": "Gozan en la bofetada que reciben como causa de ella"}],
    "r108": [{"tipo": "chicos traviesos", "descripcion": "Gozan en la bofetada"}],
    "r111": [{"tipo": "moscas", "descripcion": "Acuden a la leche como los otros a la obra"}],
    "r122": [{"tipo": "Antígona", "descripcion": "El derecho no escrito e infalible de los dioses"}]
}

# Momentos dialécticos del Capítulo V
MOMENTOS_RAZON = [
    "transición desde la autoconciencia",
    "la razón como certeza de ser toda realidad",
    "idealismo abstracto",
    "la categoría simple",
    "razón observadora",
    "observación de la naturaleza",
    "observación de lo orgánico",
    "teleología externa",
    "fracaso de la observación",
    "observación de la autoconciencia",
    "leyes lógicas",
    "leyes psicológicas",
    "fisiognómica",
    "frenología",
    "el espíritu es un hueso",
    "crítica de la frenología",
    "juicio infinito",
    "razón práctica",
    "el reino de la ética",
    "la vida de un pueblo",
    "el placer y la necesidad",
    "la necesidad como destino",
    "la ley del corazón",
    "el desvarío de la infatuación",
    "la lucha de todos contra todos",
    "el curso del mundo",
    "la virtud",
    "el caballero de la virtud",
    "derrota de la virtud",
    "la individualidad real",
    "el círculo del obrar",
    "la obra",
    "la cosa misma (Sache)",
    "distinción Ding/Sache",
    "el mutuo engaño",
    "la conciencia honrada",
    "la sustancia espiritual",
    "razón legisladora",
    "crítica de los imperativos",
    "razón examinadora",
    "tautología formal",
    "propiedad y no-propiedad",
    "la ley inmediata",
    "Antígona",
    "tránsito al Espíritu"
]

# Metáforas clave del Capítulo V
METAFORAS_RAZON = [
    "razón", "certeza", "realidad", "observación", "naturaleza", "orgánico",
    "teleología", "frenología", "cráneo", "hueso", "placer", "necesidad",
    "destino", "corazón", "ley", "virtud", "curso del mundo", "individualidad",
    "cosa misma", "reino animal", "espíritu", "legislador", "examinador",
    "categoría", "juicio infinito", "bofetada", "agujero", "brújula",
    "Solón", "Lichtenberg", "Fausto", "Antígona", "moscas", "orinar"
]

# -------------------------------------------------------------------
# FUNCIÓN PARA CARGAR EL CAPÍTULO V
# -------------------------------------------------------------------

def cargar_capitulo5(sistema, analisis):
    """Procesa todos los fragmentos del capítulo 5 y actualiza la figura de la razón."""
    
    if "razon" not in sistema.figuras:
        fig_razon = FiguraPhenomenologica(
            id="RAZ",
            nombre="Razón",
            tipo_figura=FiguraConciencia.RAZON,
            etapa=EtapaFenomenologica.RAZON,
            texto_original="",
            experiencia_conciencia="",
            verdad_aparece="",
            verdad_real="",
            contradiccion_interna="",
            leccion_dialectica="",
            metáforas_clave=[],
            ejemplos_concretos=[],
            momentos_dialecticos=[],
            ironia_linguistica="",
            perspectiva_dual={},
            notas_analisis=[]
        )
        sistema.figuras["razon"] = fig_razon
    else:
        fig_razon = sistema.figuras["razon"]
    
    print("\n📖 Cargando Capítulo V: Razón")
    print("-" * 40)
    
    for frag in FRAGMENTOS_CAPITULO5:
        frag_id = frag["id"]
        texto = frag["texto"]
        pagina = frag["pagina"]
        
        if fig_razon.texto_original:
            fig_razon.texto_original += "\n\n" + texto
        else:
            fig_razon.texto_original = texto
        
        nota = NOTAS_RAZON.get(frag_id, f"Fragmento {frag_id} (p{pagina})")
        fig_razon.notas_analisis.append(nota)
        
        if frag_id in EJEMPLOS_RAZON:
            for ej in EJEMPLOS_RAZON[frag_id]:
                if ej not in fig_razon.ejemplos_concretos:
                    fig_razon.ejemplos_concretos.append(ej)
        
        resultado = analisis.procesar_fragmento(frag_id, texto, "V. Razón")
        print(f"   Procesado {frag_id} (p{pagina}): {', '.join(resultado['conceptos_nuevos'][:3]) if resultado['conceptos_nuevos'] else 'sin conceptos'}...")
    
    fig_razon.experiencia_conciencia = (
        "La razón es la certeza de la conciencia de ser toda realidad. "
        "Esta certeza debe demostrarse a través de la observación y la acción. "
        "La razón observadora busca encontrarse en la naturaleza, en lo orgánico y en la autoconciencia misma, "
        "pero fracasa en cada intento, culminando en el absurdo de la frenología (el espíritu es un hueso). "
        "La razón pasa entonces a la acción práctica: busca la satisfacción en el placer, pero choca con la necesidad; "
        "pretende realizar la ley del corazón, pero cae en el desvarío; se refugia en la virtud, pero es derrotada por el curso del mundo. "
        "Finalmente, la razón se comprende a sí misma como individualidad real, cuya obra es la 'cosa misma' (Sache), "
        "que la conecta con los otros en un juego de mutuo engaño. "
        "Los intentos de legislar y examinar leyes fracasan por su formalismo vacío. "
        "La razón descubre entonces que su verdad no está en el individuo aislado, sino en la sustancia ética, "
        "en las leyes inmediatas de un pueblo, como las de Antígona. Este es el tránsito al Espíritu."
    )
    
    fig_razon.verdad_aparece = (
        "La verdad parece ser la certeza de que el mundo es racional y que la conciencia puede encontrarse en él, "
        "ya sea mediante la observación, la acción o la legislación moral."
    )
    
    fig_razon.verdad_real = (
        "La verdad de la razón no es la contemplación ni la acción individual aislada, "
        "sino el reconocimiento de que la sustancia ética (la comunidad, el pueblo) es la realidad de la razón. "
        "La 'cosa misma' es la obra que trasciende al individuo y lo conecta con los otros, "
        "pero solo en la vida ética de un pueblo alcanza la razón su verdadera realidad."
    )
    
    fig_razon.contradiccion_interna = (
        "La razón quiere encontrarse en la naturaleza, pero la naturaleza es indiferente. "
        "Quiere realizar su ideal en el mundo, pero el curso del mundo la derrota. "
        "La obra del individuo es para otros, y solo en el reconocimiento mutuo alcanza su verdad, "
        "pero ese reconocimiento se revela como un juego de engaños. "
        "Las leyes morales pretendidamente universales resultan vacías o tautológicas. "
        "La razón solo se reconcilia consigo misma cuando abandona la pretensión de fundamentar la ética "
        "y acepta las leyes inmediatas de la comunidad."
    )
    
    fig_razon.superacion_hacia = ["Espíritu"]
    
    fig_razon.leccion_dialectica = (
        "La razón enseña que la certeza de ser toda realidad debe demostrarse en la acción y en la comunidad. "
        "El individuo solo alcanza su verdad cuando su obra es reconocida por otros, "
        "pero este reconocimiento no es inmediato sino que pasa por figuras de engaño y conflicto. "
        "Las leyes morales abstractas son insuficientes; la verdadera eticidad es la vida concreta de un pueblo. "
        "Este es el paso al Espíritu."
    )
    
    fig_razon.metáforas_clave = list(set(fig_razon.metáforas_clave + METAFORAS_RAZON))
    fig_razon.momentos_dialecticos = list(set(fig_razon.momentos_dialecticos + MOMENTOS_RAZON))
    
    fig_razon.ironia_linguistica = (
        "La razón cree encontrarse en la naturaleza, pero la frenología le muestra que, según ella, el espíritu sería un hueso. "
        "Cree realizar su ideal en el mundo, pero el curso del mundo la derrota una y otra vez. "
        "La conciencia honrada cree ocuparse de la cosa misma, pero solo se ocupa de sí misma. "
        "La razón legisladora pretende dar leyes universales, pero solo produce tautologías. "
        "Finalmente, la razón descubre que su verdad no está en sus construcciones, sino en lo que simplemente es: "
        "las leyes no escritas de Antígona."
    )
    
    fig_razon.perspectiva_dual = {
        "para_ella": "Busca demostrar que es toda realidad, primero observando, luego actuando, luego legislando.",
        "para_nosotros": "Vemos que su verdad no está en la contemplación ni en el individuo aislado, sino en la comunidad ética, en el Espíritu."
    }
    
    sistema.transicionar("Espíritu", "La razón alcanza su verdad en la sustancia ética, que es el Espíritu.")
    analisis.estado_actual = "Espíritu"
    
    print(f"\n✅ Capítulo V procesado: {len(FRAGMENTOS_CAPITULO5)} fragmentos, {len(fig_razon.momentos_dialecticos)} momentos dialécticos.")
    
    return fig_razon


# -------------------------------------------------------------------
# FUNCIONES PARA CARGAR LOS CAPÍTULOS
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# FUNCIONES PARA CARGAR LOS CAPÍTULOS
# -------------------------------------------------------------------

def cargar_capitulo1(sistema, analisis):
    """Procesa todos los fragmentos del capítulo 1 y actualiza la figura de la certeza sensible."""
    
    if "certeza_sensible" not in sistema.figuras:
        fig_cs = FiguraPhenomenologica(
            id="CS",
            nombre="Certeza sensible",
            tipo_figura=FiguraConciencia.CONCIENCIA_SENSIBLE,
            etapa=EtapaFenomenologica.CONCIENCIA,
            texto_original="",
            experiencia_conciencia="",
            verdad_aparece="",
            verdad_real="",
            contradiccion_interna="",
            leccion_dialectica="",
            metáforas_clave=[],
            ejemplos_concretos=[],
            momentos_dialecticos=[],
            ironia_linguistica="",
            perspectiva_dual={},
            notas_analisis=[]
        )
        sistema.figuras["certeza_sensible"] = fig_cs
    else:
        fig_cs = sistema.figuras["certeza_sensible"]
    
    print("\n📖 Cargando Capítulo I: Certeza sensible")
    print("-" * 40)
    
    for frag in FRAGMENTOS_CAPITULO1:
        frag_id = frag["id"]
        texto = frag["texto"]
        pagina = frag["pagina"]
        
        if fig_cs.texto_original:
            fig_cs.texto_original += "\n\n" + texto
        else:
            fig_cs.texto_original = texto
        
        nota = NOTAS_CERTEZA_SENSIBLE.get(frag_id, f"Fragmento {frag_id} (p{pagina})")
        fig_cs.notas_analisis.append(nota)
        
        if frag_id in EJEMPLOS_CERTEZA_SENSIBLE:
            for ej in EJEMPLOS_CERTEZA_SENSIBLE[frag_id]:
                if ej not in fig_cs.ejemplos_concretos:
                    fig_cs.ejemplos_concretos.append(ej)
        
        resultado = analisis.procesar_fragmento(frag_id, texto, "I. Certeza sensible")
        print(f"   Procesado {frag_id} (p{pagina}): {', '.join(resultado['conceptos_nuevos'][:3]) if resultado['conceptos_nuevos'] else 'sin conceptos'}...")
    
    fig_cs.experiencia_conciencia = (
        "La conciencia comienza creyendo que su saber es inmediato y que capta lo singular en su ser puro. "
        "Al intentar fijar el 'ahora' y el 'aquí', descubre que estos se desvanecen; se repliega entonces en el 'yo', "
        "pero también el yo resulta universal. Finalmente, intenta mostrar el ahora, pero al mostrarlo ya no es. "
        "A lo largo de todo el proceso, la conciencia pretende lo singular pero siempre termina enunciando lo universal."
    )
    
    fig_cs.verdad_aparece = "El puro ser, el esto, el yo, la inmediatez."
    
    fig_cs.verdad_real = (
        "La verdad de la certeza sensible es el universal, que emerge de la negación de los particulares. "
        "El ahora y el aquí son universales; el yo también. La inmediatez es siempre mediada. "
        "El lenguaje dice lo universal cuando la conciencia quiere decir lo singular. "
        "La certeza sensible misma es el movimiento de mostrarse y desvanecerse."
    )
    
    fig_cs.contradiccion_interna = (
        "Pretende inmediatez pero todo es mediado; quiere lo singular pero dice lo universal; "
        "busca un objeto estable pero encuentra desaparición; se refugia en el yo pero el yo es universal; "
        "intenta mostrar el ahora pero al mostrarlo ya no es."
    )
    
    fig_cs.superacion_hacia = ["Percepción"]
    
    fig_cs.leccion_dialectica = (
        "La certeza sensible enseña que lo singular no se puede fijar ni en el objeto ni en el sujeto; "
        "su verdad es el universal, que es la negación de todos los ahora y aquí particulares. "
        "La conciencia debe abandonar esta figura y pasar a la percepción, donde el objeto será una cosa con propiedades."
    )
    
    fig_cs.metáforas_clave = list(set(fig_cs.metáforas_clave + METAFORAS_CERTEZA_SENSIBLE))
    fig_cs.momentos_dialecticos = list(set(fig_cs.momentos_dialecticos + MOMENTOS_CERTEZA_SENSIBLE))
    
    fig_cs.ironia_linguistica = (
        "El lenguaje es lo más verdadero: dice 'yo', 'ahora', 'aquí' como universales cuando la conciencia pretende lo singular. "
        "El acto de mostrar destruye lo inmediato. Los animales, con su acción, muestran la verdad práctica: devoran lo sensible."
    )
    
    fig_cs.perspectiva_dual = {
        "para_ella": "Cree que puede atrapar lo singular mediante la mostración o el repliegue en el yo.",
        "para_nosotros": "Vemos que el movimiento mismo de la certeza sensible es su verdad: el universal."
    }
    
    sistema.transicionar("Percepción", "La certeza sensible se supera hacia la percepción.")
    analisis.estado_actual = "Percepción"
    
    print(f"\n✅ Capítulo I procesado: {len(FRAGMENTOS_CAPITULO1)} fragmentos, {len(fig_cs.momentos_dialecticos)} momentos dialécticos.")
    
    return fig_cs


def cargar_capitulo2(sistema, analisis):
    """Procesa todos los fragmentos del capítulo 2 y actualiza la figura de la percepción."""
    
    if "percepcion" not in sistema.figuras:
        fig_perc = FiguraPhenomenologica(
            id="PERC",
            nombre="Percepción",
            tipo_figura=FiguraConciencia.PERCEPCION,
            etapa=EtapaFenomenologica.CONCIENCIA,
            texto_original="",
            experiencia_conciencia="",
            verdad_aparece="",
            verdad_real="",
            contradiccion_interna="",
            leccion_dialectica="",
            metáforas_clave=[],
            ejemplos_concretos=[],
            momentos_dialecticos=[],
            ironia_linguistica="",
            perspectiva_dual={},
            notas_analisis=[]
        )
        sistema.figuras["percepcion"] = fig_perc
    else:
        fig_perc = sistema.figuras["percepcion"]
    
    print("\n📖 Cargando Capítulo II: La Percepción")
    print("-" * 40)
    
    for frag in FRAGMENTOS_CAPITULO2:
        frag_id = frag["id"]
        texto = frag["texto"]
        pagina = frag["pagina"]
        
        if fig_perc.texto_original:
            fig_perc.texto_original += "\n\n" + texto
        else:
            fig_perc.texto_original = texto
        
        nota = NOTAS_PERCEPCION.get(frag_id, f"Fragmento {frag_id} (p{pagina})")
        fig_perc.notas_analisis.append(nota)
        
        if frag_id in EJEMPLOS_PERCEPCION:
            for ej in EJEMPLOS_PERCEPCION[frag_id]:
                if ej not in fig_perc.ejemplos_concretos:
                    fig_perc.ejemplos_concretos.append(ej)
        
        resultado = analisis.procesar_fragmento(frag_id, texto, "II. La percepción")
        print(f"   Procesado {frag_id} (p{pagina}): {', '.join(resultado['conceptos_nuevos'][:3]) if resultado['conceptos_nuevos'] else 'sin conceptos'}...")
    
    fig_perc.experiencia_conciencia = (
        "La conciencia percibiente considera que el objeto es una cosa universal con múltiples cualidades, "
        "independiente de ella. El percibir es un movimiento inconstante y no esencial, mientras que el objeto "
        "es lo esencial y simple. Sin embargo, al analizar la cosa (como la sal), descubre que es a la vez una "
        "y múltiple. Intenta resolver la contradicción atribuyendo la multiplicidad a sus sentidos o distribuyéndola "
        "entre varias cosas, pero la contradicción persiste. La propiedad esencial, que debía garantizar la unidad, "
        "lleva a la relación con lo otro y la cosa se derrumba. La conciencia se da cuenta de que su percibir no es "
        "puro, sino que incluye su reflexión. Finalmente, la percepción se revela como un juego de abstracciones "
        "vacías que conducen al entendimiento."
    )
    
    fig_perc.verdad_aparece = (
        "La verdad parece ser la cosa como médium universal que reúne múltiples propiedades indiferentes, "
        "o bien la cosa como uno excluyente con una propiedad esencial."
    )
    
    fig_perc.verdad_real = (
        "La percepción muestra que la cosa es una unidad contradictoria de uno y múltiple, de ser para sí y ser para otro. "
        "Los intentos de resolver esta contradicción (mediante el 'también', el 'en tanto que', la distinción esencial/accidental) "
        "fracasan. La verdad es que el objeto de la percepción es inestable y se supera a sí mismo, dando paso a una "
        "universalidad afectada de contraposición, que será el objeto del entendimiento."
    )
    
    fig_perc.contradiccion_interna = (
        "La percepción afirma que la cosa es una unidad simple, pero también que contiene múltiples propiedades indiferentes. "
        "La unidad de la cosa (el 'uno') y la multiplicidad de propiedades (el 'también') se contraponen. "
        "La propiedad esencial, que debía garantizar la independencia, implica la relación con lo otro. "
        "La conciencia oscila entre atribuir la unidad al objeto o a sí misma, sin lograr un objeto estable."
    )
    
    fig_perc.superacion_hacia = ["Entendimiento"]
    
    fig_perc.leccion_dialectica = (
        "La percepción enseña que no hay cosa estable; toda determinación implica su contrario y conduce a la superación. "
        "La conciencia debe elevarse al entendimiento, donde la verdad no será una cosa sino una ley, una fuerza, "
        "un universal que contiene la diferencia en sí mismo."
    )
    
    fig_perc.metáforas_clave = list(set(fig_perc.metáforas_clave + METAFORAS_PERCEPCION))
    fig_perc.momentos_dialecticos = list(set(fig_perc.momentos_dialecticos + MOMENTOS_PERCEPCION))
    
    fig_perc.ironia_linguistica = (
        "La conciencia usa el 'también' y el 'en tanto que' para separar lo uno de lo múltiple, "
        "pero estos recursos revelan la contradicción no resuelta. El lenguaje pretende fijar la cosa, "
        "pero la cosa se derrumba. La ironía es que la percepción, que se creía el conocimiento más rico, "
        "es en realidad el juego de las abstracciones más pobres."
    )
    
    fig_perc.perspectiva_dual = {
        "para_ella": "Cree que la cosa es una unidad de propiedades independientes, y que su percibir es puro.",
        "para_nosotros": "Vemos que la cosa es una contradicción viva, y que la conciencia proyecta en ella sus propias abstracciones."
    }
    
    sistema.transicionar("Entendimiento", "La percepción se supera hacia el entendimiento.")
    analisis.estado_actual = "Entendimiento"
    
    print(f"\n✅ Capítulo II procesado: {len(FRAGMENTOS_CAPITULO2)} fragmentos, {len(fig_perc.momentos_dialecticos)} momentos dialécticos.")
    
    return fig_perc


def cargar_capitulo3(sistema, analisis):
    """Procesa todos los fragmentos del capítulo 3 y actualiza la figura del entendimiento."""
    
    if "entendimiento" not in sistema.figuras:
        fig_ent = FiguraPhenomenologica(
            id="ENT",
            nombre="Entendimiento",
            tipo_figura=FiguraConciencia.ENTENDIMIENTO,
            etapa=EtapaFenomenologica.CONCIENCIA,
            texto_original="",
            experiencia_conciencia="",
            verdad_aparece="",
            verdad_real="",
            contradiccion_interna="",
            leccion_dialectica="",
            metáforas_clave=[],
            ejemplos_concretos=[],
            momentos_dialecticos=[],
            ironia_linguistica="",
            perspectiva_dual={},
            notas_analisis=[]
        )
        sistema.figuras["entendimiento"] = fig_ent
    else:
        fig_ent = sistema.figuras["entendimiento"]
    
    print("\n📖 Cargando Capítulo III: Fuerza y Entendimiento")
    print("-" * 40)
    
    for frag in FRAGMENTOS_CAPITULO3:
        frag_id = frag["id"]
        texto = frag["texto"]
        pagina = frag["pagina"]
        
        if fig_ent.texto_original:
            fig_ent.texto_original += "\n\n" + texto
        else:
            fig_ent.texto_original = texto
        
        nota = NOTAS_ENTENDIMIENTO.get(frag_id, f"Fragmento {frag_id} (p{pagina})")
        fig_ent.notas_analisis.append(nota)
        
        if frag_id in EJEMPLOS_ENTENDIMIENTO:
            for ej in EJEMPLOS_ENTENDIMIENTO[frag_id]:
                if ej not in fig_ent.ejemplos_concretos:
                    fig_ent.ejemplos_concretos.append(ej)
        
        resultado = analisis.procesar_fragmento(frag_id, texto, "III. Fuerza y entendimiento")
        print(f"   Procesado {frag_id} (p{pagina}): {', '.join(resultado['conceptos_nuevos'][:3]) if resultado['conceptos_nuevos'] else 'sin conceptos'}...")
    
    fig_ent.experiencia_conciencia = (
        "La conciencia (entendimiento) contempla el juego de fuerzas y postula un mundo interior suprasensible como verdad del fenómeno. "
        "Busca leyes que den cuenta de la constancia en el cambio, pero descubre que estas leyes son tautológicas. "
        "El mundo suprasensible, aunque vacío en principio, se llena con la ley, pero esta ley no agota la manifestación. "
        "La explicación científica se revela como un movimiento tautológico que solo refleja la actividad del entendimiento. "
        "Surge entonces el mundo invertido, donde las determinaciones se invierten, mostrando que lo opuesto es lo mismo. "
        "Finalmente, la infinitud emerge como la verdad: la unidad de los opuestos, el movimiento de auto-repulsión y auto-reconciliación. "
        "La conciencia se acerca a reconocer que este movimiento es su propia esencia, preparando el tránsito a la autoconciencia."
    )
    
    fig_ent.verdad_aparece = (
        "La verdad parece ser el mundo suprasensible de leyes, luego el mundo invertido, y finalmente la infinitud."
    )
    
    fig_ent.verdad_real = (
        "La verdad del entendimiento es la infinitud: la unidad de los opuestos, el ser que se relaciona consigo mismo a través de la negación. "
        "El mundo suprasensible es el fenómeno en cuanto fenómeno; el mundo invertido es la auto-inversión de lo mismo. "
        "La infinitud es el concepto de la autoconciencia. La conciencia ha estado contemplando su propia esencia sin saberlo."
    )
    
    fig_ent.contradiccion_interna = (
        "La fuerza es una pero se manifiesta como dualidad; el mundo suprasensible es vacío pero se llena con leyes; "
        "la ley es constante pero el fenómeno cambia; el mundo invertido muestra que lo opuesto es lo mismo; "
        "la infinitud es la unidad de la contradicción."
    )
    
    fig_ent.superacion_hacia = ["Autoconciencia"]
    
    fig_ent.leccion_dialectica = (
        "El entendimiento culmina en la infinitud: la unidad de los opuestos, el movimiento de auto-repulsión y auto-reconciliación. "
        "Este es el concepto de la autoconciencia. La conciencia debe ahora abandonar la actitud contemplativa y volverse sobre sí misma."
    )
    
    fig_ent.metáforas_clave = list(set(fig_ent.metáforas_clave + METAFORAS_ENTENDIMIENTO))
    fig_ent.momentos_dialecticos = list(set(fig_ent.momentos_dialecticos + MOMENTOS_ENTENDIMIENTO))
    
    fig_ent.ironia_linguistica = (
        "El entendimiento creía descubrir leyes en un mundo suprasensible, pero al final descubre que ese mundo "
        "es la infinitud, que no es otra cosa que la estructura de su propia actividad. La verdad era él mismo. "
        "La explicación científica es un diálogo de la conciencia consigo misma disfrazado de conocimiento objetivo."
    )
    
    fig_ent.perspectiva_dual = {
        "para_ella": "Contempla el juego de fuerzas, las leyes, el mundo invertido como algo externo, objetivo.",
        "para_nosotros": "Vemos que ese juego es la autoexteriorización del concepto; la conciencia se acerca a sí misma; la infinitud es su propia esencia."
    }
    
    sistema.transicionar("Autoconciencia", "La infinitud es el concepto de la autoconciencia. La conciencia se vuelve hacia sí misma.")
    analisis.estado_actual = "Autoconciencia"
    
    print(f"\n✅ Capítulo III procesado: {len(FRAGMENTOS_CAPITULO3)} fragmentos, {len(fig_ent.momentos_dialecticos)} momentos dialécticos.")
    
    return fig_ent


def cargar_capitulo4(sistema, analisis):
    """Procesa todos los fragmentos del capítulo 4 y actualiza la figura de la autoconciencia."""
    
    if "autoconciencia" not in sistema.figuras:
        fig_ac = FiguraPhenomenologica(
            id="AC",
            nombre="Autoconciencia",
            tipo_figura=FiguraConciencia.AUTOCONCIENCIA,
            etapa=EtapaFenomenologica.AUTOCONCIENCIA,
            texto_original="",
            experiencia_conciencia="",
            verdad_aparece="",
            verdad_real="",
            contradiccion_interna="",
            leccion_dialectica="",
            metáforas_clave=[],
            ejemplos_concretos=[],
            momentos_dialecticos=[],
            ironia_linguistica="",
            perspectiva_dual={},
            notas_analisis=[]
        )
        sistema.figuras["autoconciencia"] = fig_ac
    else:
        fig_ac = sistema.figuras["autoconciencia"]
    
    print("\n📖 Cargando Capítulo IV: Autoconciencia")
    print("-" * 40)
    
    for frag in FRAGMENTOS_CAPITULO4:
        frag_id = frag["id"]
        texto = frag["texto"]
        pagina = frag["pagina"]
        
        if fig_ac.texto_original:
            fig_ac.texto_original += "\n\n" + texto
        else:
            fig_ac.texto_original = texto
        
        nota = NOTAS_AUTOCONCIENCIA.get(frag_id, f"Fragmento {frag_id} (p{pagina})")
        fig_ac.notas_analisis.append(nota)
        
        if frag_id in EJEMPLOS_AUTOCONCIENCIA:
            for ej in EJEMPLOS_AUTOCONCIENCIA[frag_id]:
                if ej not in fig_ac.ejemplos_concretos:
                    fig_ac.ejemplos_concretos.append(ej)
        
        resultado = analisis.procesar_fragmento(frag_id, texto, "IV. Autoconciencia")
        print(f"   Procesado {frag_id} (p{pagina}): {', '.join(resultado['conceptos_nuevos'][:3]) if resultado['conceptos_nuevos'] else 'sin conceptos'}...")
    
    fig_ac.experiencia_conciencia = (
        "La autoconciencia emerge de la infinitud del entendimiento como certeza de sí misma. "
        "Inicialmente se presenta como apetencia (Begierde) que busca superar la vida independiente. "
        "La vida se revela como un proceso infinito de figuras que se afirman devorando lo universal y disolviéndose. "
        "La autoconciencia, como género, se enfrenta a la vida y busca su satisfacción aniquilando el objeto, "
        "pero esta satisfacción es momentánea y reproduce el objeto, conduciendo a la necesidad de otra autoconciencia. "
        "La autoconciencia solo alcanza su verdad cuando es reconocida por otra autoconciencia. "
        "Surge así el concepto del espíritu: el yo que es nosotros y el nosotros que es yo. "
        "Se inicia el movimiento del reconocimiento, donde la autoconciencia se duplica y se enfrenta a otra. "
        "El hacer es recíproco y duplicado, como en el juego de fuerzas. "
        "Para alcanzar el verdadero reconocimiento, las autoconciencias deben luchar a muerte, arriesgando la vida. "
        "Pero la muerte cancela el reconocimiento; la verdad no está en la muerte sino en la superación de la vida en una relación desigual. "
        "Surgen así dos figuras: el señor (conciencia independiente) y el siervo (conciencia dependiente). "
        "El señor es la conciencia que es para sí por medio de otra conciencia (el siervo). "
        "El señor goza a través del trabajo del siervo, pero el reconocimiento es unilateral; la verdad del señorío no está en el señor, sino en el siervo. "
        "El siervo, a través del temor a la muerte y del trabajo formativo, alcanza una forma superior de autoconciencia: se reconoce en el producto de su trabajo. "
        "Este proceso conduce a la libertad de la autoconciencia en el pensamiento. "
        "Aparecen entonces las figuras del estoicismo (libertad abstracta), el escepticismo (negación de todo ser otro) y la conciencia desventurada (duplicación interna no resuelta). "
        "La conciencia desventurada se escinde entre un inmutable (Dios) y su propio ser mudable, y busca inútilmente la unidad a través de diversas actitudes: el fervor devoto, el trabajo y la mortificación. "
        "Finalmente, a través del silogismo mediado por el sacerdote, la renuncia a la propiedad y al goce, y la experiencia del sepulcro vacío, la conciencia alcanza la representación de la razón: la certeza de ser, en su singularidad, absoluta en sí o toda realidad. Este es el tránsito a la Razón (Capítulo V)."
    )
    
    fig_ac.verdad_aparece = "La verdad parece ser la certeza de sí misma alcanzada mediante el reconocimiento por otra autoconciencia."
    
    fig_ac.verdad_real = (
        "La verdad de la autoconciencia no es la aniquilación momentánea del objeto, ni la muerte del otro, sino el reconocimiento recíproco. "
        "La lucha a muerte es necesaria pero no suficiente; la muerte lo cancela. "
        "La verdadera figura que emerge es la del señor y el siervo, donde el reconocimiento es unilateral, pero prepara el camino para una forma superior de autoconciencia a través del trabajo. "
        "El trabajo formativo y el temor conducen a la libertad interior del pensamiento. "
        "El estoicismo, escepticismo y conciencia desventurada son intentos fallidos de alcanzar la unidad, que finalmente se anuncia como Razón."
    )
    
    fig_ac.contradiccion_interna = (
        "La autoconciencia busca afirmarse aniquilando el objeto, pero al hacerlo, el objeto (la vida) es independiente y se reproduce, "
        "mostrando que la autoconciencia no puede alcanzar la verdad por sí sola; necesita de otra autoconciencia. "
        "Al enfrentarse a otra, debe luchar a muerte, pero la muerte cancela el reconocimiento. "
        "El señor cree ser independiente, pero depende del trabajo del siervo; el siervo, aunque dependiente, encuentra en el trabajo el camino a la verdadera independencia. "
        "La conciencia desventurada se escinde entre lo inmutable y lo mudable, sin lograr la unidad."
    )
    
    fig_ac.superacion_hacia = ["Razón"]
    
    fig_ac.leccion_dialectica = (
        "La autoconciencia, en su figura inicial de apetencia, descubre que la negación del objeto no basta para su verdad. "
        "La vida es el proceso que la remite a otra autoconciencia, iniciando el camino del reconocimiento. "
        "La lucha a muerte muestra que la vida es tan esencial como la pura autoconciencia. "
        "La relación señor-siervo es la primera figura del reconocimiento, pero unilateral; la verdad del señorío no está en el señor, sino en el trabajo del siervo. "
        "El trabajo formativo y el temor preparan la libertad interior. "
        "El estoicismo, escepticismo y conciencia desventurada muestran la insuficiencia de la libertad abstracta. "
        "La conciencia desventurada, en su desgarramiento, anuncia la Razón como la certeza de ser toda realidad."
    )
    
    fig_ac.metáforas_clave = list(set(fig_ac.metáforas_clave + METAFORAS_AUTOCONCIENCIA))
    fig_ac.momentos_dialecticos = list(set(fig_ac.momentos_dialecticos + MOMENTOS_AUTOCONCIENCIA))
    
    fig_ac.ironia_linguistica = (
        "La autoconciencia cree afirmarse aniquilando lo otro, pero en realidad se condena a la insatisfacción y depende de lo otro. "
        "Cuando se enfrenta a otra autoconciencia, cree perderse, pero solo así puede encontrarse verdaderamente. "
        "El señor cree ser libre, pero depende del trabajo del siervo; el siervo, en su aparente sujeción, encuentra la libertad a través del trabajo. "
        "La conciencia desventurada cree acercarse a Dios mediante la renuncia, pero solo se enajena más."
    )
    
    fig_ac.perspectiva_dual = {
        "para_ella": "Busca la certeza de sí mediante la superación del objeto independiente; luego busca el reconocimiento a través de la lucha; luego se establece en la relación señor-siervo; luego se refugia en el pensamiento; finalmente anhela la unión con lo inmutable.",
        "para_nosotros": "Vemos que la verdad del reconocimiento es recíproca, que el trabajo del siervo es la clave para la verdadera independencia, y que la conciencia desventurada es la antesala de la Razón."
    }
    
    sistema.transicionar("Razón", "La autoconciencia alcanza la representación de la razón y se supera hacia ella.")
    analisis.estado_actual = "Razón"
    
    print(f"\n✅ Capítulo IV procesado: {len(FRAGMENTOS_CAPITULO4)} fragmentos, {len(fig_ac.momentos_dialecticos)} momentos dialécticos.")
    
    return fig_ac


def cargar_capitulo5(sistema, analisis):
    """Procesa todos los fragmentos del capítulo 5 y actualiza la figura de la razón."""
    
    if "razon" not in sistema.figuras:
        fig_razon = FiguraPhenomenologica(
            id="RAZ",
            nombre="Razon",
            tipo_figura=FiguraConciencia.RAZON,
            etapa=EtapaFenomenologica.RAZON,
            texto_original="",
            experiencia_conciencia="",
            verdad_aparece="",
            verdad_real="",
            contradiccion_interna="",
            leccion_dialectica="",
            metáforas_clave=[],
            ejemplos_concretos=[],
            momentos_dialecticos=[],
            ironia_linguistica="",
            perspectiva_dual={},
            notas_analisis=[]
        )
        sistema.figuras["razon"] = fig_razon
    else:
        fig_razon = sistema.figuras["razon"]
    
    print("\n📖 Cargando Capítulo V: Razón")
    print("-" * 40)
    
    # Asegurarse de que FRAGMENTOS_CAPITULO5 existe
    try:
        fragmentos = FRAGMENTOS_CAPITULO5
    except NameError:
        print("❌ Error: FRAGMENTOS_CAPITULO5 no está definido.")
        return fig_razon
    
    for frag in fragmentos:
        frag_id = frag["id"]
        texto = frag["texto"]
        pagina = frag["pagina"]
        
        if fig_razon.texto_original:
            fig_razon.texto_original += "\n\n" + texto
        else:
            fig_razon.texto_original = texto
        
        try:
            nota = NOTAS_RAZON.get(frag_id, f"Fragmento {frag_id} (p{pagina})")
        except NameError:
            nota = f"Fragmento {frag_id} (p{pagina})"
        fig_razon.notas_analisis.append(nota)
        
        try:
            if frag_id in EJEMPLOS_RAZON:
                for ej in EJEMPLOS_RAZON[frag_id]:
                    if ej not in fig_razon.ejemplos_concretos:
                        fig_razon.ejemplos_concretos.append(ej)
        except NameError:
            pass
        
        resultado = analisis.procesar_fragmento(frag_id, texto, "V. Razón")
        print(f"   Procesado {frag_id} (p{pagina}): {', '.join(resultado['conceptos_nuevos'][:3]) if resultado['conceptos_nuevos'] else 'sin conceptos'}...")
    
    fig_razon.experiencia_conciencia = (
        "La razón es la certeza de la conciencia de ser toda realidad. "
        "Esta certeza debe demostrarse a través de la observación y la acción. "
        "La razón observadora busca encontrarse en la naturaleza, en lo orgánico y en la autoconciencia misma, "
        "pero fracasa en cada intento, culminando en el absurdo de la frenología (el espíritu es un hueso). "
        "La razón pasa entonces a la acción práctica: busca la satisfacción en el placer, pero choca con la necesidad; "
        "pretende realizar la ley del corazón, pero cae en el desvarío; se refugia en la virtud, pero es derrotada por el curso del mundo. "
        "Finalmente, la razón se comprende a sí misma como individualidad real, cuya obra es la 'cosa misma' (Sache), "
        "que la conecta con los otros en un juego de mutuo engaño. "
        "Los intentos de legislar y examinar leyes fracasan por su formalismo vacío. "
        "La razón descubre entonces que su verdad no está en el individuo aislado, sino en la sustancia ética, "
        "en las leyes inmediatas de un pueblo, como las de Antígona. Este es el tránsito al Espíritu."
    )
    
    fig_razon.verdad_aparece = (
        "La verdad parece ser la certeza de que el mundo es racional y que la conciencia puede encontrarse en él, "
        "ya sea mediante la observación, la acción o la legislación moral."
    )
    
    fig_razon.verdad_real = (
        "La verdad de la razón no es la contemplación ni la acción individual aislada, "
        "sino el reconocimiento de que la sustancia ética (la comunidad, el pueblo) es la realidad de la razón. "
        "La 'cosa misma' es la obra que trasciende al individuo y lo conecta con los otros, "
        "pero solo en la vida ética de un pueblo alcanza la razón su verdadera realidad."
    )
    
    fig_razon.contradiccion_interna = (
        "La razón quiere encontrarse en la naturaleza, pero la naturaleza es indiferente. "
        "Quiere realizar su ideal en el mundo, pero el curso del mundo la derrota. "
        "La obra del individuo es para otros, y solo en el reconocimiento mutuo alcanza su verdad, "
        "pero ese reconocimiento se revela como un juego de engaños. "
        "Las leyes morales pretendidamente universales resultan vacías o tautológicas. "
        "La razón solo se reconcilia consigo misma cuando abandona la pretensión de fundamentar la ética "
        "y acepta las leyes inmediatas de la comunidad."
    )
    
    fig_razon.superacion_hacia = ["Espíritu"]
    
    fig_razon.leccion_dialectica = (
        "La razón enseña que la certeza de ser toda realidad debe demostrarse en la acción y en la comunidad. "
        "El individuo solo alcanza su verdad cuando su obra es reconocida por otros, "
        "pero este reconocimiento no es inmediato sino que pasa por figuras de engaño y conflicto. "
        "Las leyes morales abstractas son insuficientes; la verdadera eticidad es la vida concreta de un pueblo. "
        "Este es el paso al Espíritu."
    )
    
    try:
        fig_razon.metáforas_clave = list(set(fig_razon.metáforas_clave + METAFORAS_RAZON))
    except NameError:
        pass
    
    try:
        fig_razon.momentos_dialecticos = list(set(fig_razon.momentos_dialecticos + MOMENTOS_RAZON))
    except NameError:
        pass
    
    fig_razon.ironia_linguistica = (
        "La razón cree encontrarse en la naturaleza, pero la frenología le muestra que, según ella, el espíritu sería un hueso. "
        "Cree realizar su ideal en el mundo, pero el curso del mundo la derrota una y otra vez. "
        "La conciencia honrada cree ocuparse de la cosa misma, pero solo se ocupa de sí misma. "
        "La razón legisladora pretende dar leyes universales, pero solo produce tautologías. "
        "Finalmente, la razón descubre que su verdad no está en sus construcciones, sino en lo que simplemente es: "
        "las leyes no escritas de Antígona."
    )
    
    fig_razon.perspectiva_dual = {
        "para_ella": "Busca demostrar que es toda realidad, primero observando, luego actuando, luego legislando.",
        "para_nosotros": "Vemos que su verdad no está en la contemplación ni en el individuo aislado, sino en la comunidad ética, en el Espíritu."
    }
    
    sistema.transicionar("Espíritu", "La razón alcanza su verdad en la sustancia ética, que es el Espíritu.")
    analisis.estado_actual = "Espíritu"
    
    print(f"\n✅ Capítulo V procesado: {len(fragmentos)} fragmentos, {len(fig_razon.momentos_dialecticos)} momentos dialécticos.")
    
    return fig_razon




# -------------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------------------------------------------

def main():
    print("=" * 70)
    print("🧠 MÁQUINA HEGELIANA – CAPÍTULOS I, II, III, IV COMPLETOS")
    print("=" * 70)
    print("Basado en la edición de W. Roces (FCE)")
    print("=" * 70)

    memoria = MemoriaDialectica()
    sistema = SistemaFenomenologicoMejorado()
    sistema.cargar_configuracion({"modo": "carga completa", "version": "Capítulos I, II y III"})

    analisis = AnalisisCorrelativo(memoria)
    analisis.cambiar_perspectiva("para nosotros")

    
    # ... inicialización ...
    cargar_capitulo1(sistema, analisis)
    cargar_capitulo2(sistema, analisis)
    cargar_capitulo3(sistema, analisis)
    cargar_capitulo4(sistema, analisis)
    cargar_capitulo5(sistema, analisis)  # <-- Asegúrate de que esta línea existe
    # ... resto del código ...

    # Mostrar resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN FINAL DEL ESTADO")
    print("=" * 70)
    print(f"Estado actual: {analisis.estado_actual}")
    print(f"Total fragmentos procesados: {len(analisis.linea_dialectica)}")
    print(f"Figuras cargadas: {list(sistema.figuras.keys())}")
    
    for nombre_figura, figura in sistema.figuras.items():
        print(f"\n📌 {figura.nombre}:")
        print(f"   • Momentos dialécticos: {len(figura.momentos_dialecticos)}")
        print(f"   • Ejemplos concretos: {len(figura.ejemplos_concretos)}")
        print(f"   • Metáforas clave: {len(figura.metáforas_clave)}")
        print(f"   • Contradicción: {figura.contradiccion_interna[:100]}...")

    # Predicción del próximo paso
    prediccion = sistema.predecir_proximo_paso(analisis.estado_actual)
    print(f"\n🔮 PRÓXIMO PASO: {prediccion.get('proximo', 'desconocido')} – {prediccion.get('razon', '')}")

    # Guardar estado
    sistema.guardar_estado("estado_hegeliano_completo.json")

    # Exportar grafo
    analisis.exportar_a_dot("camino_hegeliano_completo.dot")

    print("\n" + "=" * 70)
    print("✅ MÁQUINA HEGELIANA – CUATRO PRIMEROS CAPÍTULOS COMPLETADOS")
    print("=" * 70)
    print("\nArchivos generados:")
    print("   • camino_hegeliano_completo.dot  (visualización del camino dialéctico)")
    print("   • estado_hegeliano_completo.json (estado completo del sistema)")
    print("\nPróximo capítulo: V – ")


if __name__ == "__main__":
    main()