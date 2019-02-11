$(document).ready(function(){
    $('.lang-list img').click(function(){
        var count = $('.skills img').length;
          if(count < 5){
            var clickedSkill = $(this);
            var skill_name = clickedSkill.attr('skill');
            console.log(skill_name)
            $(this).remove();
            $('div.skills').append(clickedSkill);
            $('div.skills').append("<input type='hidden' class='skill' value='" + skill_name + "'>")
        }
    });
});
$(document).ready(function(){
    $('img').on('click', 'div.skills', function(){
        var clickedSkill = $(this);
        var skill_input = $('input').filter(clickedSkill.skill);
        console.log(skill_input);
        $(this).remove();
        $('div.lang_list').append(clickedSkill);
    });
});