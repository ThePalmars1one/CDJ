document.addEventListener('DOMContentLoaded', function() {
    var elemssidenav = document.querySelectorAll('.sidenav');
    var instancessidenav = M.Sidenav.init(elemssidenav);
   });

   $(document).ready(function() {
    $('.link').click(function() {
      $('.link').removeClass('active-link');
      $(this).addClass('active-link');
    });
  });
