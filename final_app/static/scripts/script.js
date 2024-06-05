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