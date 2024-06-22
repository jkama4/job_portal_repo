document.addEventListener('DOMContentLoaded', () => {
    // Update the search bar with the selected job role
    const jobSelect = document.getElementById('job-select');
    const searchInput = document.getElementById('search-input');

    function updateSearchInput() {
        if (jobSelect.value === "Job Title" || jobSelect.value === "") {
            searchInput.value = "";
            searchInput.placeholder = "Search for a Job";
        } else {
            searchInput.value = jobSelect.options[jobSelect.selectedIndex].text;
            searchInput.placeholder = jobSelect.options[jobSelect.selectedIndex].text;
        }
    }

    jobSelect.addEventListener('change', updateSearchInput);
    updateSearchInput(); // Ensure the initial state is set

    // Enable city selection only when a country is selected
    const countrySelect = document.getElementById('country-select');
    const citySelect = document.getElementById('city-select');

    countrySelect.addEventListener('change', () => {
        if (countrySelect.value) {
            citySelect.disabled = false;
            populateCities(countrySelect.value);
        } else {
            citySelect.disabled = true;
            citySelect.innerHTML = '<option value="">City</option>';
        }
    });

    // Populate countries and cities
    const countries = {
        "Albania": ["Tirana", "Durrës", "Vlorë", "Shkodër", "Fier"],
        "Andorra": ["Andorra la Vella", "Escaldes-Engordany", "Encamp", "Sant Julià de Lòria", "La Massana"],
        "Austria": ["Vienna", "Graz", "Linz", "Salzburg", "Innsbruck"],
        "Belgium": ["Brussels", "Antwerp", "Ghent", "Charleroi", "Liège"],
        "Bosnia and Herzegovina": ["Sarajevo", "Banja Luka", "Tuzla", "Zenica", "Mostar"],
        "Bulgaria": ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"],
        "Croatia": ["Zagreb", "Split", "Rijeka", "Osijek", "Zadar"],
        "Cyprus": ["Nicosia", "Limassol", "Larnaca", "Famagusta", "Paphos"],
        "Czech Republic": ["Prague", "Brno", "Ostrava", "Plzeň", "Liberec"],
        "Denmark": ["Copenhagen", "Aarhus", "Odense", "Aalborg", "Esbjerg"],
        "Estonia": ["Tallinn", "Tartu", "Narva", "Pärnu", "Kohtla-Järve"],
        "Finland": ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"],
        "Greece": ["Athens", "Thessaloniki", "Patras", "Heraklion", "Larissa"],
        "Hungary": ["Budapest", "Debrecen", "Szeged", "Miskolc", "Pécs"],
        "Iceland": ["Reykjavik", "Kopavogur", "Hafnarfjordur", "Akureyri", "Reykjanesbær"],
        "Ireland": ["Dublin", "Cork", "Limerick", "Galway", "Waterford"],
        "Italy": ["Rome", "Milan", "Naples", "Turin", "Palermo"],
        "Latvia": ["Riga", "Daugavpils", "Liepaja", "Jelgava", "Jurmala"],
        "Liechtenstein": ["Vaduz", "Schaan", "Balzers", "Triesen", "Eschen"],
        "Lithuania": ["Vilnius", "Kaunas", "Klaipeda", "Šiauliai", "Panevėžys"],
        "Luxembourg": ["Luxembourg City", "Esch-sur-Alzette", "Differdange", "Dudelange", "Ettelbruck"],
        "Malta": ["Valletta", "Birkirkara", "Mosta", "Qormi", "Sliema"],
        "Moldova": ["Chișinău", "Tiraspol", "Bălți", "Bender", "Rîbnița"],
        "Monaco": ["Monaco"],
        "Montenegro": ["Podgorica", "Nikšić", "Herceg Novi", "Pljevlja", "Bijelo Polje"],
        "Netherlands": ["Amsterdam", "Rotterdam", "The Hague", "Utrecht", "Eindhoven"],
        "North Macedonia": ["Skopje", "Bitola", "Kumanovo", "Prilep", "Tetovo"],
        "Norway": ["Oslo", "Bergen", "Stavanger", "Trondheim", "Drammen"],
        "Poland": ["Warsaw", "Krakow", "Łódź", "Wrocław", "Poznań"],
        "Portugal": ["Lisbon", "Porto", "Amadora", "Braga", "Coimbra"],
        "Romania": ["Bucharest", "Cluj-Napoca", "Timișoara", "Iași", "Constanța"],
        "San Marino": ["San Marino", "Serravalle", "Borgo Maggiore", "Domagnano", "Fiorentino"],
        "Serbia": ["Belgrade", "Novi Sad", "Niš", "Kragujevac", "Subotica"],
        "Slovakia": ["Bratislava", "Košice", "Prešov", "Žilina", "Nitra"],
        "Slovenia": ["Ljubljana", "Maribor", "Celje", "Kranj", "Velenje"],
        "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza"],
        "Sweden": ["Stockholm", "Gothenburg", "Malmö", "Uppsala", "Västerås"],
        "Switzerland": ["Zurich", "Geneva", "Basel", "Bern", "Lausanne"],
        "Ukraine": ["Kyiv", "Kharkiv", "Odessa", "Dnipro", "Lviv"],
        "United Kingdom": ["London", "Birmingham", "Manchester", "Glasgow", "Liverpool"],
        "Vatican City": ["Vatican City"]
    };

    function populateCountries() {
        for (let country in countries) {
            const option = document.createElement('option');
            option.value = country;
            option.textContent = country;
            countrySelect.appendChild(option);
        }
    }

    function populateCities(selectedCountry) {
        const cities = countries[selectedCountry];
        citySelect.innerHTML = '<option value="">City</option>';
        cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            option.textContent = city;
            citySelect.appendChild(option);
        });
    }

    populateCountries();

    // Handle form submission to append location to the URL
    const searchForm = document.getElementById('search-form');
    searchForm.addEventListener('submit', function(event) {
        const country = countrySelect.value;
        const city = citySelect.value;
        const location = city ? city : country;
        const query = searchInput.value;

        if (location) {
            event.preventDefault();
            const queryString = `q=${query}&country=${country}&city=${city}`;
            window.location.href = `${searchForm.action}?${queryString}`;
        }
    });
});

