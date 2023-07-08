function setup_questoes_tipo() {
    var select = document.getElementById("tipo");
    var me = document.getElementById("alternativas_div");
    var ce = document.getElementById("certo_errado_div");
    var ca = document.getElementById("resposta_div");

    select.addEventListener("change", ()=>{
        switch (select.value) {
            case "ME":
                me.hidden=false;
                ce.hidden=true;
                ca.hidden=true;

                break;
            case "CA":
                me.hidden=true;
                ce.hidden=true;
                ca.hidden=false;

                break;
            case "CE":
                me.hidden=true;
                ce.hidden=false;
                ca.hidden=true;

                break;
            default:
                me.hidden=true;
                ce.hidden=true;
                ca.hidden=true;

                break;
        }
    }) 
}
document.onload = setup_questoes_tipo();
