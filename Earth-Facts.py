"""Display random Earth facts from the Bootprint API."""

import requests

EARTH_FACT_URL = "https://api.bootprint.space/fact/earth"
REQUEST_TIMEOUT_SECONDS = 5


class EarthFactError(RuntimeError):
    """Raised when an Earth fact cannot be retrieved or validated."""


def fetch_earth_fact():
    """Request one Earth fact and return it as a clean string."""
    try:
        response = requests.get(
            EARTH_FACT_URL,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

    except requests.Timeout as exc:
        raise EarthFactError("The request timed out. Please try again.") from exc

    except requests.ConnectionError as exc:
        raise EarthFactError("The Earth-fact service could not be reached.") from exc

    except requests.HTTPError as exc:
        status_code = (
            exc.response.status_code if exc.response is not None else "unknown"
        )

        raise EarthFactError(
            f"The Earth-fact service returned HTTP status {status_code}."
        ) from exc

    except requests.RequestException as exc:
        raise EarthFactError("An unexpected network error occurred.") from exc

    try:
        data = response.json()

    except ValueError as exc:
        raise EarthFactError(
            "The Earth-fact service returned invalid JSON data."
        ) from exc

    if not isinstance(data, dict):
        raise EarthFactError("The Earth-fact service returned an unexpected response.")

    fact = data.get("fact")

    if not isinstance(fact, str) or not fact.strip():
        raise EarthFactError("The Earth-fact service did not return a usable fact.")

    return fact.strip()


def ask_yes_no(prompt):
    """Prompt until the user enters yes/y or no/n."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in {"yes", "y"}:
            return True

        if answer in {"no", "n"}:
            return False

        print("Please answer yes/y or no/n.")


def main():
    """Run the Earth Facts command-line program."""
    seen_facts = 0

    try:
        # Outer loop
        while True:
            see_space = (
                input("Would you like to see some Earth facts? [yes/no] ")
                .strip()
                .lower()
            )

            if see_space in {"no", "n"}:
                print("No worries, goodbye!")
                return 0

            if see_space not in {"yes", "y"}:
                print("Please answer yes/y or no/n.")
                continue

            # Inner loop
            while True:
                try:
                    fact = fetch_earth_fact()

                except EarthFactError as exc:
                    print(f"\nError: {exc}")

                    retry_request = ask_yes_no(
                        "Would you like to retry the request? [yes/no] "
                    )

                    if retry_request:
                        continue

                    print("Goodbye!")
                    return 1

                seen_facts += 1

                print(f"\nEarth fact #{seen_facts}:")
                print(fact)

                see_more = ask_yes_no(
                    "\nWould you like to see another Earth fact? [yes/no] "
                )

                if not see_more:
                    fact_word = "fact" if seen_facts == 1 else "facts"

                    print(
                        f"Hope you learned something new! "
                        f"You viewed {seen_facts} Earth {fact_word}."
                    )

                    return 0

    except KeyboardInterrupt:
        print("\nUser exit. Goodbye!")
        return 130

    except EOFError:
        print("\nInput ended. Goodbye!")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
