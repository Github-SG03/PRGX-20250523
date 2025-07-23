for i in range(10,14):
    print(''',
        {
            "fieldname": "FIM_CIGRTAX_STR_DATE'''+str(i)+'''1",
            "fieldrules": [
                {
                    "rulename": "date_convert",
                    "args": [
                        {
                            "argvalue": "yyyyMMdd"
                        }
                    ]
                }
            ]
        },
        {
            "fieldname": "FIM_CIGRTAX_STR_DATE'''+str(i)+'''2",
            "fieldrules": [
                {
                    "rulename": "date_convert",
                    "args": [
                        {
                            "argvalue": "yyyyMMdd"
                        }
                    ]
                }
            ]
        },
        {
            "fieldname": "FIM_CIGRTAX_STR_DATE'''+str(i)+'''3",
            "fieldrules": [
                {
                    "rulename": "date_convert",
                    "args": [
                        {
                            "argvalue": "yyyyMMdd"
                        }
                    ]
                }
            ]
        },
        {
            "fieldname": "FIM_CIGRTAX_STR_DATE'''+str(i)+'''4",
            "fieldrules": [
                {
                    "rulename": "date_convert",
                    "args": [
                        {
                            "argvalue": "yyyyMMdd"
                        }
                    ]
                }
            ]
        }''')
