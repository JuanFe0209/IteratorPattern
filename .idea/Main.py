from Employee import Employee
from Organization import Organization

if __name__ == "__main__":
    # Crear empleados
    ceo = Employee("Juan", "CEO")
    manager = Employee("Camilo", "Manager")
    admin = Employee("Santiago", "Administrativo")
    ejec_ventas = Employee("David", "Ejecutivo de ventas")
    j_marketing = Employee("Mariana", "Jefa de Marketing")
    marketing = Employee("Valentina", "Marketing")

    # Construir la jerarquía organizacional
    ceo.add_subordinate(manager)
    ceo.add_subordinate(admin)
    manager.add_subordinate(ejec_ventas)
    manager.add_subordinate(j_marketing)
    j_marketing.add_subordinate(marketing)

    # Crear la organización
    org = Organization(ceo)

    # Recorrer la organización
    for employee in org:
        print(employee)
