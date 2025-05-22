// Initialization for ES Users
import { Collapse, Ripple, initMDB, Modal, Input} from "mdb-ui-kit";

initMDB({ Collapse, Ripple, Modal, Input });

let form = document.querySelector("#login-form");

let saveBtn = document.querySelector("#button-form");

window.addEventListener("load", function () {
    console.log("aoba");
})

saveBtn.addEventListener("click", function (e) {
    console.log("Button clicked");
    saveBtn.setAttribute("disabled", "true");
    saveBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>`;
    setTimeout(() => {
    form.submit();
    }, 1000);
});