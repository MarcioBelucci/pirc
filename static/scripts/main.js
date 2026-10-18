const checkboxes = document.querySelectorAll('input[name="ids"]');
const button = document.querySelector('#compare-btn');

function updateButton() {
  const checkedCount = document.querySelectorAll('input[name="ids"]:checked').length;  
  button.disabled = checkedCount < 2 || checkedCount > 3;
}

checkboxes.forEach((control) => {
  control.addEventListener("change", updateButton);
});

updateButton();