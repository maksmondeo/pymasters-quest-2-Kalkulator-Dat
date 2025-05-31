import contextlib
from datetime import datetime, timedelta, timezone


def main() -> None:
    while True:
        print(
            "\nWybierz opcję:\n1. Oblicz różnicę między datami\n2. Dodaj dni do daty\n3. Odejmij dni od daty\n4. Zakończ program\n"
        )
        choice = input("Wybierz opcję (1-4): ")

        with contextlib.suppress(ValueError):
            choice = int(choice)

        if not isinstance(choice, int):
            print("\nNieprawidłowy wybór! Spróbuj ponownie.\n")
        else:
            break

    match choice:
        case 1:
            date1 = input("\nPodaj pierwszą datę (DD/MM/YYYY): ")
            date2 = input("Podaj drugą datę (DD/MM/YYYY): ")

            try:
                date1_time = datetime.strptime(date1, "%d/%m/%Y").astimezone(
                    timezone.utc
                )
                date2_time = datetime.strptime(date2, "%d/%m/%Y").astimezone(
                    timezone.utc
                )
                print(
                    f"\nRóżnica : {abs(date1_time - date2_time).days} dni\n(od {date1} do {date2})"
                )
            except ValueError:
                print("\nPodano nieprawidłowe daty!")

        case 2:
            date1 = input("\nPodaj datę (DD/MM/YYYY): ")
            days = input("\nPodaj ilość dni do dodania: ")

            try:
                date1_time = datetime.strptime(date1, "%d/%m/%Y").astimezone(
                    timezone.utc
                )
                new_date = date1_time + timedelta(days=int(days))
                formatted_date = new_date.strftime("%d/%m/%Y")

                print(
                    f"\nData po dodaniu dni: {formatted_date}\n({days} dni po {date1})"
                )
            except ValueError:
                print("\nPodano nieprawidłowe daty!")

    input("\nNaciśnij aby kontynuować...")
    main()


if __name__ == "__main__":
    print(
        "\n=== Kalkulator Dat ===\nWitaj! Ten program pomoże Ci w obliczeniach z datami."
    )
    main()
