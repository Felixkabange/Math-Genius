const React = require('react');
const ReactDOM = require('react-dom');

function App() {
    document.addEventListener('DOMContentLoaded', function() {
        const additionButton = document.querySelector('#addition');
        const multiplicationButton = document.querySelector('#multiplication');
        const subtractionButton = document.querySelector('#substraction');
        const divisionButton = document.querySelector('#division');

        const additionGame = document.querySelector('#addition-game');
        const multiplicationGame = document.querySelector('#multiplication-game');
        const subtractionGame = document.querySelector('#substraction-game');
        const divisionGame = document.querySelector('#division-game');

        function hideAllGames() {
            additionGame.style.display = 'none';
            multiplicationGame.style.display = 'none';
            subtractionGame.style.display = 'none';
            divisionGame.style.display = 'none';
        }

        additionButton.addEventListener('click', () => {
            hideAllGames();
            additionGame.style.display = 'block';
        });

        multiplicationButton.addEventListener('click', () => {
            hideAllGames();
            multiplicationGame.style.display = 'block';
        });

        subtractionButton.addEventListener('click', () => {
            hideAllGames();
            subtractionGame.style.display = 'block';
        });

        divisionButton.addEventListener('click', () => {
            hideAllGames();
            divisionGame.style.display = 'block';
        });
    });

    return (
        <div>
            {"Hello react"}
        </div>
    );
}

ReactDOM.render(<App />, document.querySelector("#app"));



