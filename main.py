import csv
import json
import pprint

import requests
from bs4 import BeautifulSoup

# Define your proxy information
username = "enter your username here"
password = "enter your password here"
proxy = f"http://{username}:{password}@gate.smartproxy.com:10000"


# Function to make requests with proxies
def make_request_with_proxy(url):
    try:
        response = requests.get(
            url, proxies={"http": proxy, "https": proxy}, timeout=None
        )
        return response

    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return None


base_url = "enter the target URL here"
all_data = []

# Open the CSV file in write mode
with open("output.csv", "a", newline="", encoding="utf-8-sig") as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    csv_writer.writerow(
        [
            "URL",
            "Titre court",
            "Résumé",
            "Lieu",
            "ISSN",
            "Edition",
            "Editeur",
            "Description",
            "A une parte",
            "Titre",
            "Auteur",
            "Année",
            "Type",
            "Pages",
            "ISBN",
            "Titre du périodique",
            "Numéro",
            "Mot-clé",
            "Thesaurus",
        ]
    )

    for item_number in range(24573, 999999):  # You can adjust the range as needed
        # Lowest number probably around 14200
        # Made it to item/21881 before crashing so start from 21880 next, 24573, 25843
        current_url = f"{base_url}{item_number}"
        print(current_url)

        # Make the request with the proxy
        response = make_request_with_proxy(current_url)

        if response is None:
            # Skip to the next iteration if there's an error with the proxy
            continue

        if "Page introuvable" in response.text:
            # Skip the page if 'Page introuvable' is present
            continue

        # Write your code below this line 👇
        profile_page = response.text
        soup = BeautifulSoup(profile_page, "html.parser")

        page_profile_dict = {}

        h4_title_19 = soup.find("h4", string="URL")
        if h4_title_19:
            profile_url = h4_title_19.find_next_sibling().get_text()
            page_profile_dict["URL"] = profile_url
        else:
            page_profile_dict["URL"] = "None"

        h4_title_18 = soup.find("h4", string="Titre court")
        if h4_title_18:
            titre_court = h4_title_18.find_next_sibling().get_text()
            page_profile_dict["Titre court"] = titre_court
        else:
            page_profile_dict["Titre court"] = "None"

        h4_title_17 = soup.find("h4", string="Résumé")
        if h4_title_17:
            resume = h4_title_17.find_next_sibling().get_text()
            page_profile_dict["Résumé"] = resume
        else:
            page_profile_dict["Résumé"] = "None"

        h4_title_16 = soup.find("h4", string="Lieu")
        if h4_title_16:
            lieu = h4_title_16.find_next_sibling().get_text()
            page_profile_dict["Lieu"] = lieu
        else:
            page_profile_dict["Lieu"] = "None"

        h4_title_15 = soup.find("h4", string="ISSN")
        if h4_title_15:
            issn = h4_title_15.find_next_sibling().get_text()
            page_profile_dict["ISSN"] = issn
        else:
            page_profile_dict["ISSN"] = "None"

        h4_title_14 = soup.find("h4", string="Edition")
        if h4_title_14:
            edition = h4_title_14.find_next_sibling().get_text()
            page_profile_dict["Edition"] = edition
        else:
            page_profile_dict["Edition"] = "None"

        h4_title_13 = soup.find("h4", string="Editeur")
        if h4_title_13:
            editeur = h4_title_13.find_next_sibling().get_text()
            page_profile_dict["Editeur"] = editeur
        else:
            page_profile_dict["Editeur"] = "None"

        h4_title_12 = soup.find("h4", string="Description")
        if h4_title_12:
            description = h4_title_12.find_next_sibling().get_text()
            page_profile_dict["Description"] = description
        else:
            page_profile_dict["***"] = "None"

        h4_title_11 = soup.find("h4", string="A une parte")
        if h4_title_11:
            a_une_parte = h4_title_11.find_next_sibling().get_text()
            page_profile_dict["A une parte"] = a_une_parte
        else:
            page_profile_dict["A une parte"] = "None"

        h4_title_8 = soup.find("h4", string="Titre")
        if h4_title_8:
            titre = h4_title_8.find_next_sibling().get_text()
            page_profile_dict["Titre"] = titre
        else:
            page_profile_dict["Titre"] = "None"

        h4_title_9 = soup.find("h4", string="Auteur")
        if h4_title_9:
            auteur = h4_title_9.find_next_sibling().get_text()
            page_profile_dict["Auteur"] = auteur
        else:
            page_profile_dict["Auteur"] = "None"

        h4_title_6 = soup.find("h4", string="Année")
        if h4_title_6:
            annee = h4_title_6.find_next_sibling().get_text()
            page_profile_dict["Année"] = annee
        else:
            page_profile_dict["Année"] = "None"

        h4_title_5 = soup.find("h4", string="Type")
        if h4_title_5:
            type = h4_title_5.find_next_sibling().get_text()
            page_profile_dict["Type"] = type
        else:
            page_profile_dict["Type"] = "None"

        h4_title_1 = soup.find("h4", string="Pages")
        if h4_title_1:
            pages = h4_title_1.find_next_sibling().get_text()
            page_profile_dict["Pages"] = pages
        else:
            page_profile_dict["Pages"] = "None"

        h4_title_2 = soup.find("h4", string="ISBN")
        if h4_title_2:
            isbn = h4_title_2.find_next_sibling().get_text()
            page_profile_dict["ISBN"] = isbn
        else:
            page_profile_dict["ISBN"] = "None"

        h4_title_3 = soup.find("h4", string="Titre du périodique")
        if h4_title_3:
            titre_du_periodique = h4_title_3.find_next_sibling()
            page_profile_dict["Titre du périodique"] = titre_du_periodique.get_text()
        else:
            page_profile_dict["Titre du périodique"] = "None"

        h4_title_4 = soup.find("h4", string="Numéro")
        if h4_title_4:
            numero = h4_title_4.find_next_sibling().get_text()
            page_profile_dict["Numéro"] = numero
        else:
            page_profile_dict["Numéro"] = "None"

        h4_title_7 = soup.find("h4", string="Mot-clé")
        if h4_title_7:
            mot_cle = h4_title_7.find_next_sibling().get_text()
            page_profile_dict["Mot-clé"] = mot_cle
        else:
            page_profile_dict["Mot-clé"] = "None"

        h4_title_10 = soup.find("h4", string="Thésaurus")
        if h4_title_10:
            thesaurus_names = [
                sibling.get_text() for sibling in h4_title_10.find_next_siblings()
            ]
            page_profile_dict["Thesaurus_names"] = thesaurus_names
            thesaurus_links = [
                "https://bibliographienumeriquedhistoiredudroit-ifg.univ-lorraine.fr/"
                + sibling2.find("a", href=True)["href"]
                for sibling2 in h4_title_10.find_next_siblings()
            ]
            thesaurus_entries = [
                f"{name} - Link to {link}"
                for name, link in zip(thesaurus_names, thesaurus_links)
            ]
            formatted_thesaurus = ", ".join(thesaurus_entries)
            page_profile_dict["Thesaurus"] = formatted_thesaurus
        else:
            page_profile_dict["Thesaurus"] = "None"

        csv_writer.writerow(
            [
                page_profile_dict.get(key, "None")
                for key in [
                    "URL",
                    "Titre court",
                    "Résumé",
                    "Lieu",
                    "ISSN",
                    "Edition",
                    "Editeur",
                    "Description",
                    "A une parte",
                    "Titre",
                    "Auteur",
                    "Année",
                    "Type",
                    "Pages",
                    "ISBN",
                    "Titre du périodique",
                    "Numéro",
                    "Mot-clé",
                    "Thesaurus",
                ]
            ]
        )

        (pprint.pprint(page_profile_dict, sort_dicts=False))

print("CSV file 'output.csv' created successfully.")
