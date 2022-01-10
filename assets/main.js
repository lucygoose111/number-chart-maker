const mainDataJSON = document.getElementById('main-data');


mainDataJSON.addEventListener('change', function() {
    let newFileReader = new FileReader();
    var file = this.files[0];
    if(file === undefined) {return;}
    var text = newFileReader.readAsText(file);
    newFileReader.onload = function() {

        let resultText = newFileReader.result;
        var json = JSON.parse(resultText);
        var squareContainer = document.getElementById('square-container');  
        let squareContainerHTML = '';

        if (json.chartType === 'num_chart') {

            for (let i=1; i <= json.number; i++) {


                if (json.numVisible === true) {

                    squareContainerHTML += '<div class="square" id="square-'+i+'">'+i+'</div>';

                }

                else if (json.numVisible === false) {

                    squareContainerHTML += '<div class="square" id="square-'+i+'"></div>';

                }

            }

            squareContainer.innerHTML = squareContainerHTML;

        }

    };
    
});