document.addEventListener('DOMContentLoaded', function() {
  const elems = document.querySelectorAll('.sidenav');
  const options = {}; // Add this line to define the options variable
  const instances = M.Sidenav.init(elems, options);
});