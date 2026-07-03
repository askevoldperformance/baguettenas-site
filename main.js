document.addEventListener('click', function (e) {
  if (e.target.closest('.nav-hamburger')) {
    document.querySelector('.nav-links').classList.toggle('open');
    return;
  }
  var navLinks = document.querySelector('.nav-links');
  if (navLinks && !e.target.closest('.nav-links') && !e.target.closest('.nav-hamburger')) {
    navLinks.classList.remove('open');
  }
});
