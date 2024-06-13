// Update the search bar with the selected job role
const jobSelect = document.getElementById('job-select');
const searchInput = document.getElementById('search-input');

function updateSearchInput() {
    console.log("Job selected: ", jobSelect.value); // Debug log

    if (jobSelect.value === "--job title--" || jobSelect.value === "") {
        console.log("Setting placeholder and value for default selection"); // Debug log
        searchInput.value = "";
        searchInput.placeholder = "Search for a Job";
    } else {
        console.log("Setting placeholder and value for job selection: ", jobSelect.value); // Debug log
        searchInput.value = jobSelect.options[jobSelect.selectedIndex].text;
        searchInput.placeholder = jobSelect.options[jobSelect.selectedIndex].text;
    }
}

jobSelect.addEventListener('change', updateSearchInput);

// Initialize the search input correctly on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log("Document loaded, initializing search input"); // Debug log
    updateSearchInput(); // Ensure the initial state is set
});

// Enable city selection only when a country is selected
const countrySelect = document.getElementById('country-select');
const citySelect = document.getElementById('city-select');

countrySelect.addEventListener('change', () => {
    if (countrySelect.value) {
        citySelect.disabled = false;
        populateCities(countrySelect.value);
    } else {
        citySelect.disabled = true;
        citySelect.innerHTML = '<option value="">--city--</option>';
    }
});

// Populate countries and cities
const countries = {
    "Netherlands": ["Amsterdam", "Rotterdam", "Utrecht"],
    "France": ["Paris", "Lyon", "Marseille"],
    "England": ["London", "Manchester", "Liverpool"]
    // Add more countries and cities here
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
    citySelect.innerHTML = '<option value="">--city--</option>';
    cities.forEach(city => {
        const option = document.createElement('option');
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    populateCountries();
});

const listenButton = document.querySelector(".listen");

listenButton?.addEventListener('click', () => {
    const contentText = document.querySelector(".para1").textContent;
    const speechSynthesis = window.speechSynthesis;
    const speechText = new SpeechSynthesisUtterance(contentText);
    speechText.lang = 'en-EN';
    speechText.rate = 1.0;
    // speechText.volume = 0.75; 
    speechSynthesis.speak(speechText);
});
