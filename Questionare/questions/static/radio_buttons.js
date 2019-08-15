$(function () {
  $(".chb").change(function() {
      $(this).siblings().filter('.chb').prop('checked', false);
      $(this).prop('checked', true);
  });
});
