let startX;
const slider = document.querySelector(".slider");

const totalSlides = 7;
let currentSlide = 1;

slider.addEventListener("touchstart", (e) => {
  startX = e.touches[0].clientX;
});

slider.addEventListener("touchend", (e) => {
  const endX = e.changedTouches[0].clientX;
  if (startX - endX > 50 && currentSlide < totalSlides) {
    // Swipe left, go to next slide
    currentSlide++;
  } else if (endX - startX > 50 && currentSlide > 1) {
    // Swipe right, go to previous slide
    currentSlide--;
  }
  document.getElementById(`btn-${currentSlide}`).checked = true;
});
