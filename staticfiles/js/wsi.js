var hintOne = $('#hintOne');

function change_over(){
  $(this).text("I'm changed!");
};

function change_out(){
  $(this).text("Insert");
};

hintOne.click(change_over)



// hintOne.addEventListener('mouseover', change_over)
// hintOne.addEventListener('mouseout', change_out)
