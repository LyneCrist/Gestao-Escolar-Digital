//  Immediately-Invoked Function Expression (IIFE)
; (atlas => {

    const nome = atlas.document.getElementById("nome");

    const telefone = atlas.document.getElementById("telefone");

    const cartaoSUS = atlas.document.getElementById("cartaoSUS");

    const rua = atlas.document.getElementById("rua");

    const numero = atlas.document.getElementById("numero");

    const complemento = atlas.document.getElementById("complemento")

    const pontoReferencia = atlas.document.getElementById("pontoReferencia")

    nome.focus();

    nome.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 50);

        event.target.value = atlas.replace(event.target.value, atlas.isAlpha);

    });

    telefone.addEventListener("input", event => {

        if (event.inputType === "insertText") {
            event.target.value = atlas.mask(event.target.value)
        }
    });

    cartaoSUS.addEventListener('input', event => {

        event.target.value = atlas.maximum(event.target.value, 15);

        event.target.value = atlas.replace(event.target.value, atlas.isNumeric);
    });

    rua.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 50);

        event.target.value = atlas.replace(event.target.value, atlas.isAlphaNumericCharacter);

    });

    numero.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 7);

        event.target.value = atlas.replace(event.target.value, atlas.isAlphaNumeric);
    });

    complemento.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 40);

        event.target.value = atlas.replace(event.target.value, atlas.isAlphaNumericCharacter);

    });

    pontoReferencia.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 40);

        event.target.value = atlas.replace(event.target.value, atlas.isAlphaNumericCharacter);

    });

    atlas.window.addEventListener('beforeunload', event => {
        console.log("Atlas sendo encerrado");
    });

})({
    document,
    window,
    "isAlpha": isAlpha,
    "isNumeric": isNumeric,
    "isAlphaNumeric": isAlphaNumeric,
    "isAlphaNumericCharacter": isAlphaNumericCharacter,
    "mask": maskPhone,
    "replace": replaceCharacter,
    "maximum": maximumCharacters
})