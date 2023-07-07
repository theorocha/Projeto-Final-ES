// AJAX para pegar as questões
function fazerRequisicao() {
    fetch('/questoes/all')
        .then(response => response.json())
        .then(data => {
            const selectElement = document.getElementById('selectedQuestions');
            
            for (const key in data) {
                console.log(data[key]);
                const optionElement = document.createElement('option');
                optionElement.value = data[key][0];
                optionElement.textContent = data[key][1];
                selectElement.appendChild(optionElement);
            }
        })
        .catch(error => {
        console.error('Ocorreu um erro na solicitação:', error);
        });
}
fazerRequisicao();
