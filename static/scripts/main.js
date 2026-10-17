const checkboxes = document.querySelectorAll('input[name="ids"]');
const button = document.querySelector('button');

checkboxes.forEach((control) => {
  control.addEventListener("change", () => {
    const checkedCount = document.querySelectorAll('input[name="ids"]:checked').length;
    button.disabled = checkedCount < 2 || checkedCount > 3;
  });
});