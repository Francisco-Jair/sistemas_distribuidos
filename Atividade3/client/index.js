const login = function () {
  const emailUser = document.querySelector("#exampleInputEmail1").value;

  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "POST",
    headers: myHeaders,
    body: JSON.stringify({ login: emailUser }),
    mode: "cors",
    cache: "default",
  };

  fetch("http://127.0.0.1:8000/login", myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        if (data.status === "OK") {
          sessionStorage.setItem("usuarioEmail", emailUser);

          botao = document.querySelector("#loginSite");
          botao.click();
        }
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
};

const caixaDeEntradaEmails = function (dados) {
  const lista = document.querySelector("#listagrupo");

  let campo = "";

  if (dados.result.length === 0) {
    console.log("Vazio");
  } else {
    for (let i = 0; i < dados.result.length; i++) {
      //list-group-item-light

      if (dados.result[i][4] == 1) {
        campo += `<a id='${dados.result[i][0]}' href="#" onclick="abrirEmail(${dados.result[i][0]})" class="list-group-item list-group-item-action list-group-item-light">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">${dados.result[i][2]} - ${dados.result[i][3]}</h5>
        </div>
        </a>
        `;
      } else {
        campo += `<a id='${dados.result[i][0]}' href="#" onclick="abrirEmail(${dados.result[i][0]})" class="list-group-item list-group-item-action">
      <div class="d-flex w-100 justify-content-between">
        <h5 class="mb-1">${dados.result[i][2]} - ${dados.result[i][3]}</h5>
      </div>
      </a>
      `;
      }
    }

    lista.innerHTML = campo;
  }
};

const caixaDeEntrada = function () {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "GET",
    headers: myHeaders,
    // body: JSON.stringify({ login: emailUser }),
    mode: "cors",
    cache: "default",
  };

  fetch("http://127.0.0.1:8000/email/caixa_entrada", myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        caixaDeEntradaEmails(data);
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
};

const sendEmail = function () {
  const destinatario = document.querySelector(
    "#exampleFormControlInput1"
  ).value;
  const assunto = document.querySelector("#exampleFormControlInput2").value;
  const corpo = document.querySelector("#exampleFormControlTextarea1").value;

  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "POST",
    headers: myHeaders,
    body: JSON.stringify({
      destinatario: destinatario,
      assunto: assunto,
      corpo: corpo,
    }),
    mode: "cors",
    cache: "default",
  };

  fetch("http://127.0.0.1:8000/enviar_email", myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        if (data.status === "OK") {
          botao = document.querySelector("#pagInicial");
          botao.click();
        }
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
};

const logout = function () {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "GET",
    headers: myHeaders,
    // body: JSON.stringify({ login: emailUser }),
    mode: "cors",
    cache: "default",
  };

  fetch("http://127.0.0.1:8000/logout", myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        if (data.status === "OK") {
          botao = document.querySelector("#logoutId");
          botao.click();
        }
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
};

const abrirEmail = function (id) {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "PUT",
    headers: myHeaders,
    // body: JSON.stringify({ login: emailUser }),
    mode: "cors",
    cache: "default",
  };

  fetch(`http://127.0.0.1:8000/email/${id}`, myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        if (data.status === "OK") {
          botao = document.querySelector("#abrirEmailid");
          botao.click();

          var dados = JSON.stringify(data.result);
          sessionStorage.setItem("chave", dados);
        }
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
};

const abrirEmailLoad = function (data) {
  document.querySelector("#remetenteID").value = data[5];
  // document.querySelector("#destinatarioId").value;
  document.querySelector("#exampleFormControlInput2").value = data[2];
  document.querySelector("#exampleFormControlTextarea1").value = data[3];
};

const deletarEmail = function () {
  deleta = JSON.parse(sessionStorage.getItem("chave"));

  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "DELETE",
    headers: myHeaders,
    // body: JSON.stringify({ login: emailUser }),
    mode: "cors",
    cache: "default",
  };

  fetch(`http://127.0.0.1:8000/email/delete/${deleta[0]}`, myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        botao = document.querySelector("#pagInicial");
        botao.click();
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
  botao = document.querySelector("#pagInicial");
  botao.click();
};

const responderEmail = function () {
  email = JSON.parse(sessionStorage.getItem("chave"));
  userEmail = email[1];

  corpo = document.querySelector("#exampleFormControlTextarea1").value;
  respostaMsg = document.querySelector("#exampleFormControlTextarea2").value;

  const res = `${corpo}\n--------------------------------------\n ${userEmail} : ${respostaMsg}`;


  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "POST",
    headers: myHeaders,
    body: JSON.stringify({
      resposta: res,
      id: email[0],
      destinatario: email[5]
    }),
    mode: "cors",
    cache: "default",
  };

  fetch("http://127.0.0.1:8000/email/resposta", myInit)
    .then(async (response) => {
      response.json().then((data) => {
        botao = document.querySelector("#pagInicial");
        botao.click();
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });
  botao = document.querySelector("#pagInicial");
  botao.click();
};

const encaminharEmail = function () {
  //encamiID
  document.querySelector("#respondID").remove();
  document.querySelector("#encamiID").remove();
  document.querySelector("#deleteID").remove();
  document.querySelector("#exampleFormControlTextarea2").remove();

  var newdiv = document.createElement("div");
  newdiv.innerHTML = `<div class="form-group">
  <label for="novoEmcaminhar">Encaminhar para</label>
  <input
    type="email"
    class="form-control"
    id="novoEmcaminhar"
    placeholder="name@example.com"
  />
  </div>
  <button id="enviarId2" type="submit" class="btn btn-primary" onclick="enviarEncaminhado()">Enviar</button>
`;
  document.getElementById("campoEmcaminhar").appendChild(newdiv);
};

const enviarEncaminhado = function () {
  const email = JSON.parse(sessionStorage.getItem("chave"));
  const paraQuem = document.querySelector("#novoEmcaminhar").value;

  corpo = `Remetente: ${email[5]}\n
  Destinatário: ${email[1]}\n
  Assunto: ${email[2]}\n
  Mensagem: ${email[3]}\n`;

  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "text/json");

  var myInit = {
    method: "POST",
    headers: myHeaders,
    body: JSON.stringify({
      destinatario: paraQuem,
      assunto: "E-mail encaminhado",
      corpo: corpo,
    }),
    mode: "cors",
    cache: "default",
  };

  fetch("http://127.0.0.1:8000/enviar_email", myInit)
    .then(async (response) => {
      // respost = await response.json();
      response.json().then((data) => {
        if (data.status === "OK") {
          botao = document.querySelector("#pagInicial");
          botao.click();
        }
      });
    })
    .catch(function (error) {
      console.log(error.message);
    });

  botao = document.querySelector("#pagInicial");
  botao.click();
};
