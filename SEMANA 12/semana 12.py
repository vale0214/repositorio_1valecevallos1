temperaturas = [
    [   # Santo Domingo
        [   # Semana 1
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   #
        [   #Quevedo
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 32}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 22}
        ]
    ]
]
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += (dia['temp'] / 7)
        print (suma)