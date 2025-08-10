document.getElementById('spinButton').addEventListener('click', function () {
    const wheel = document.getElementById('wheel');
    const segments = document.querySelectorAll('.segment');
    const resultText = document.getElementById('result');

    // Simulate a random spin, but always make it land on "You win!"
    let randomDegree = Math.floor(Math.random() * 360); // Random degree to simulate spinning
    wheel.style.transition = 'transform 4s ease-out';  // Smooth transition

    // Rotate the wheel
    wheel.style.transform = `rotate(${randomDegree + 1800}deg)`; // 1800deg for multiple spins

    // Set the result after the wheel stops
    setTimeout(function () {
        resultText.textContent = "Result: You win!";
    }, 4000);  // After 4 seconds, display "You win!"
});
