import contextlib
from datetime import datetime, timezone


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
                date1time = datetime.strptime(date1, "%d/%m/%Y").astimezone(
                    timezone.utc
                )
                date2time = datetime.strptime(date2, "%d/%m/%Y").astimezone(
                    timezone.utc
                )
                print(
                    f"\nRóżnica : {abs(date1time - date2time).days} dni\n(od {date1} do {date2})"
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
