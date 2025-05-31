import contextlib
import sys
from datetime import datetime, timedelta, timezone


def parse_date(date_str: str) -> datetime:
    formats = ["%d/%m/%Y", "%Y-%m-%d", "%d.%m.%Y", "%d-%m-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).astimezone(timezone.utc)
        except ValueError:  # noqa: PERF203
            continue
    msg = "Nieprawidłowy format daty!"
    raise ValueError(msg)


def main() -> None:
    while True:
        print(
            "\nWybierz opcję:\n1. Oblicz różnicę między datami\n2. Dodaj dni do daty\n3. Odejmij dni od daty\n4. Zakończ program\n"
        )
        choice = input("Wybierz opcję (1-4): ")

        with contextlib.suppress(ValueError):
            choice = int(choice)

        if not isinstance(choice, int) or choice not in range(1, 5):
            print("\nNieprawidłowy wybór! Spróbuj ponownie.\n")
        else:
            break

    match choice:
        case 1:
            date1 = input("\nPodaj pierwszą datę (DD/MM/YYYY): ")
            date2 = input("Podaj drugą datę (DD/MM/YYYY): ")

            try:
                date1_time = parse_date(date1)
                date2_time = parse_date(date2)
                print(
                    f"\nRóżnica : {abs(date1_time - date2_time).days} dni\n(od {date1} do {date2})"
                )
            except ValueError:
                print("\nPodano nieprawidłowe daty!")

        case 2:
            date1 = input("\nPodaj datę (DD/MM/YYYY): ")
            days = input("\nPodaj ilość dni do dodania: ")

            try:
                date1_time = parse_date(date1)
                new_date = date1_time + timedelta(days=int(days))
                formatted_date = new_date.strftime("%d/%m/%Y")

                print(
                    f"\nData po dodaniu dni: {formatted_date}\n({days} dni po {date1})"
                )
            except ValueError:
                print("\nPodano nieprawidłowe daty!")

        case 3:
            date1 = input("\nPodaj datę (DD/MM/YYYY): ")
            days = input("\nPodaj ilość dni do odjęcia: ")

            try:
                date1_time = parse_date(date1)
                new_date = date1_time - timedelta(days=int(days))
                formatted_date = new_date.strftime("%d/%m/%Y")

                print(
                    f"\nData po odjęciu dni: {formatted_date}\n({days} dni przed {date1})"
                )
            except ValueError:
                print("\nPodano nieprawidłowe daty!")
        case 4:
            print("\nDziękuję za skorzystanie z Generatora Haseł!\n")
            sys.exit()

    input("\nNaciśnij aby kontynuować...")
    main()


if __name__ == "__main__":
    print(
        "\n=== Kalkulator Dat ===\nWitaj! Ten program pomoże Ci w obliczeniach z datami."
    )
    main()
