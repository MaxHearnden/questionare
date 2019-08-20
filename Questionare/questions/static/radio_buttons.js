$(function () {
  $(".chb").change(function() {
      $(this).siblings().filter('.chb').prop('checked', false);
      $(this).prop('checked', true);
  });
});
$(function () {
    $(".stb").change(function(){
        $(this).siblings().filter(".form-control").show()
    });
    $(".htb").change(function() {
        $(this).siblings().filter(".form-control").hide()
    });
});