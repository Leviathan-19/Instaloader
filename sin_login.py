from services.instagram_service import InstagramService
from utils.excel_exporter import export_to_excel

def main():
    username = input("Ingrese el usuario de Instagram: ")

    service = InstagramService()

    print("Modo sin login")

    posts = service.get_posts(username)

    if not posts:
        print("No se pudieron obtener datos")
        return

    print("Exportando a Excel")
    export_to_excel(posts)

if __name__ == "__main__":
    main()