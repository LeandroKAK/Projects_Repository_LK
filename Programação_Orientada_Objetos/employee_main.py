from employee_class import Employee, FullTime, Hourly

if __name__ == '__main__':
    # Testes da Fulltime
    Employee1 = FullTime("Pedro", "Almeida")
    Employee2 = FullTime("Mariana", "Mazali", 5000, 500)

    print('='*20)

    print('Nome do empregado 2:\n ', Employee2.get_first_name())
    print('Sobrenome do empregado 2:\n ', Employee2.get_last_name())
    print('Nome completo do empregado 2:\n ', Employee2.full_name())

    print('='*20)

    print('Salario base do empregado 1:\n ', Employee1.base_salary)
    print('Bonus salarial do empregado 1:\n ', Employee1.bonus)
    print('Salário total do empregado 1:\n ', Employee1.compute_salary())

    print('='*20)

    print('Alterando nome do empregado 1 de:\n ', Employee1.get_first_name())
    Employee1.set_first_name('Frederico')
    print('Para:\n ', Employee1.get_first_name())

    print('='*20)

    print('Alterando salário base do empregado 2 de:\n ', Employee2.get_base_salary())
    Employee2.set_base_salary('-20')
    print('Para:\n ', Employee2.get_base_salary())

    print('Alterando salário base do empregado 2 de:\n ', Employee2.get_base_salary())
    Employee2.set_base_salary('50000')
    print('Para:\n ', Employee2.get_base_salary())

    print('='*20)

    # Testes da Hourly
    Employee3 = Hourly("Danilo", "Ferreira", 100)
    Employee4 = Hourly("Damylle", "Soares", 30, 5)

    print('='*20)

    print('Nome do empregado 3:\n ', Employee3.get_first_name())
    print('Sobrenome do empregado 3:\n ', Employee3.get_last_name())
    print('Nome completo do empregado 3:\n ', Employee3.full_name())

    print('='*20)

    print('Salario por hora do empregado 4:\n ', Employee4.get_salaryhour())
    print('Horas trabalhadas do empregado 4:\n ', Employee4.get_time())
    print('Salário total do empregado 4:\n ', Employee4.compute_salary())

    print('='*20)

    print('Alterando nome do empregado 3 de:\n ', Employee3.get_first_name())
    Employee1.set_first_name('Murilo')
    print('Para:\n ', Employee1.get_first_name())

    print('='*20)

    print('Alterando salário por hora do empregado 4 de:\n ', Employee4.get_salaryhour())
    Employee4.set_salaryhour('-20')
    print('Para:\n ', Employee4.get_salaryhour())

    print('Alterando salário por hora do empregado 4 de:\n ', Employee4.get_salaryhour())
    Employee4.set_salaryhour('20')
    print('Para:\n ', Employee4.get_salaryhour())