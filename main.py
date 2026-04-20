from services.instagram_service import InstagramService
from utils.excel_exporter import export_to_excel

def main():
    username = input("Ingrese el usuario de Instagram: ")

    service = InstagramService()

    print("Iniciando sesión...")
    service.login()

    print("Obteniendo datos...")
    posts = service.get_posts(username)

    print("Exportando a Excel...")
    export_to_excel(posts)

    print("Proceso finalizado")

if __name__ == "__main__":
    main()