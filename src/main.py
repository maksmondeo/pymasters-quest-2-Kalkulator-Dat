import contextlib
import sys
from calendar import weekday
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
            "\nWybierz opcję:\n1. Oblicz różnicę między datami\n2. Dodaj dni do daty\n3. Odejmij dni od daty\n4. Oblicz wiek\n5. Sprawdź dzień tygodnia\n6. Zakończ program\n"
        )
        choice = input("Wybierz opcję (1-6): ")

        with contextlib.suppress(ValueError):
            choice = int(choice)

        if not isinstance(choice, int) or choice not in range(1, 7):
            print("\nNieprawidłowy wybór! Spróbuj ponownie.\n")
        else:
            break

    match choice:
        case 1:
            date1 = input("\nPodaj pierwszą datę (różne formaty akceptowane): ")
            date2 = input("Podaj drugą datę (różne formaty akceptowane): ")

            try:
                date1_time = parse_date(date1)
                date2_time = parse_date(date2)
                print(
                    f"\nRóżnica : {abs(date1_time - date2_time).days} dni\n(od {date1} do {date2})"
                )
            except ValueError:
                print("\nPodano nieprawidłowe daty!")

        case 2:
            date1 = input("\nPodaj datę (różne formaty akceptowane): ")
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
            date1 = input("\nPodaj datę (różne formaty akceptowane): ")
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
            try:
                date_today = datetime.now(tz=timezone.utc)
                date1 = ""

                while True:
                    date1 = input(
                        "\nPodaj datę urodzenia (różne formaty akceptowane): "
                    )
                    date1 = parse_date(date1)
                    if date_today < date1:
                        print("\nNie podano przeszłej daty.")
                    else:
                        break

                age_years = date_today.year - date1.year
                age_months = date_today.month - date1.month
                age_days = date_today.day - date1.day

                if not age_years:
                    age_years = ""
                elif age_years == 1:
                    age_years = "1 rok "
                elif 2 <= age_years % 10 <= 4 and not (12 <= age_years % 100 <= 14):  # noqa: PLR2004
                    age_years = f"{age_years} lata "
                else:
                    age_years = f"{age_years} lat "

                if not age_months:
                    age_months = ""
                elif age_months == 1:
                    age_months = "1 miesiąc "
                elif age_months in [2, 3, 4]:
                    age_months = f"{age_months} miesiące "
                else:
                    age_months = f"{age_months} miesięcy "

                if not age_days:
                    age_days = ""
                elif age_days == 1:
                    age_days = "1 dzień "
                else:
                    age_days = f"{age_days} dni "

                print(f"\nTwój wiek: {age_years}{age_months}{age_days}")
            except ValueError:
                print("\nPodano nieprawidłową datę!")

        case 5:
            date_today = datetime.now(tz=timezone.utc)
            days = {
                0: "Poniedziałek",
                1: "Wtorek",
                2: "Środa",
                3: "Czwartek",
                4: "Piątek",
                5: "Sobota",
                6: "Niedziela",
            }

            print(
                f"\nDziś jest: {days[weekday(date_today.year, date_today.month, date_today.day)]}"
            )

        case 6:
            print("\nDziękuję za skorzystanie z Kalkluatora dat!\n")
            sys.exit()

    input("\nNaciśnij aby kontynuować...")
    main()


if __name__ == "__main__":
    print(
        "\n=== Kalkulator Dat ===\nWitaj! Ten program pomoże Ci w obliczeniach z datami."
    )
    main()
