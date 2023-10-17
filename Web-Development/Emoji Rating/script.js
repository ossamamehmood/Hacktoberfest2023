const starsEl = document.querySelectorAll(".fa-star");
const emojisEl = document.querySelectorAll(".far");
const colorsList = ["red", "orange", "lightblue", "lightGreen", "green"];

updateRating(0);

starsEl.forEach((starEl, index) => {
  starEl.addEventListener("click", () => {
    updateRating(index);
  });
});

function updateRating(index) {
  starsEl.forEach((starEl, idx) => {
    if (idx <= index) {
      starEl.classList.add("active");
    } else {
      starEl.classList.remove("active");
    }
  });
  emojisEl.forEach((emojiEl) => {
    emojiEl.style.transform = `translateX(-${index * 50}px)`;
    emojiEl.style.color = colorsList[index];
  });
}
