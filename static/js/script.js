function SearchTag(checkbox) {

    document.searchProjects.submit();
}

function SearchTagCard(tag) {


    document.querySelectorAll('input[type=checkbox]').forEach(el =>{
        el.checked = false;
        if (el.value == tag.value) {
            el.checked = true;
        };
    });


    document.searchProjects.submit();
}