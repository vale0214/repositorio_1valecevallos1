temperaturas = [
    [   # Santo Domingo
        [   # Semana 1
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 23}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 40},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 17},
            {"dia": "Domingo", "temp": 19}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 37},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 29},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 33},
            {"dia": "Viernes", "temp": 32},
            {"dia": "Sábado", "temp": 30},
            {"dia": "Domingo", "temp": 29}
        ]
    ],
    [   #
        [   #Quevedo
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 31},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 30},
            {"dia": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 33},
            {"dia": "Sábado", "temp": 37},
            {"dia": "Domingo", "temp": 39}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 40},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 31},
            {"dia": "Jueves", "temp": 38},
            {"dia": "Viernes", "temp": 36},
            {"dia": "Sábado", "temp": 29},
            {"dia": "Domingo", "temp": 32}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 10},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 21},
            {"dia": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 22},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 21},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 15},
            {"dia": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 11},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 31},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 24},
            {"dia": "Miércoles", "temp": 31},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 37},
            {"dia": "Domingo", "temp": 22}
        ]
    ]
]
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += (dia['temp'] / 7)
        print (suma)