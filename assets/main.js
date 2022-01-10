const mainDataJSON = document.getElementById('main-data');


mainDataJSON.addEventListener('change', function() {

    let jsonFileName = 'mainData.json';
    let newFileReader = new FileReader();
    var file = this.files[0];
    if(file === undefined) {return;}
    var text = newFileReader.readAsText(file);
    
    if (file.name === jsonFileName) {

        newFileReader.onload = function() {

            let resultText = newFileReader.result;
            var json = JSON.parse(resultText);
            var squareContainer = document.getElementById('square-container');  
            let squareContainerHTML = '';

            for (let i=1; i <= json.number; i++) {


                if (json.numVisible === true) {

                    squareContainerHTML += '<div class="square" id="square-'+i+'">'+i+'</div>';

                }

                else if (json.numVisible === false) {

                    squareContainerHTML += '<div class="square" id="square-'+i+'"></div>';

                }

            }

            squareContainer.innerHTML = squareContainerHTML;
        

        };

    }
    
});