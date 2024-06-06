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

document.getElementById('search-btn').addEventListener('click', function() {
    const query = document.getElementById('job-search').value;
    searchJobs(query);
});

function searchJobs(query) {
    // This function will handle fetching job listings from the Google Jobs API
    // and updating the DOM with the results
    // Example:
    // fetch(`https://jobs.googleapis.com/v3/projects/your-project-id/tenants/your-tenant-id/jobQueries:search?query=${query}`)
    //     .then(response => response.json())
    //     .then(data => displayJobs(data));
}

function displayJobs(jobs) {
    const jobsContainer = document.getElementById('jobs-container');
    jobsContainer.innerHTML = ''; // Clear any existing jobs

    jobs.forEach(job => {
        const jobItem = document.createElement('div');
        jobItem.classList.add('job-item');
        jobItem.innerHTML = `
            <h3>${job.title}</h3>
            <p>${job.description}</p>
            <p><strong>Location:</strong> ${job.location}</p>
            <p><strong>Company:</strong> ${job.company}</p>
        `;
        jobsContainer.appendChild(jobItem);
    });
}
