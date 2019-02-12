$(document).ready(function(){
    $('.skill-list img').click(function(){
        var count = $('.skills img').length;
          if(count < 5){
            var clickedSkill = $(this);
            var skill_name = clickedSkill.attr('skill');
            $(this).remove();
            $('div.skills').append(clickedSkill);
            $('div.skills').append("<input type='hidden' id='" + skill_name + "' class='skill' value='" + skill_name + "'>")
        }
    });
    $('.skills').on('click', '.skill', function(){
        var clickedSkill = $(this);
        var skillname = $(this).attr('skill')
        var hiddenInput = document.getElementById(skillname);
        hiddenInput.remove();
        $(this).remove();
        $('div.skill-list').append(clickedSkill);
    });
});
