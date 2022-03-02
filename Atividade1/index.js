const municipios = document.querySelector("#municipios");

var t;

const dadosDoEstado = function (dados) {
  let dadosEstado = dados;
  //   console.log(dadosEstado);
  //   t = dadosEstado;

  //   mapeando somente os nomes
  const nomes = dadosEstado.map((item) => {
    return { name: item.nome };
  });

  //   Inserir na tela
  inserirTabela = document.getElementsByTagName("tbody")[0];
  inserirTabela.innerHTML = `${dadosEstado
    .map(
      (item, indice) => `<tr>
  <th scope="row">${indice+1}</th>
  <td>${municipios.value}</td>
  <td>${item.nome}</td>
    </tr>`
    )
    .join("")}`;
};

municipios.addEventListener("blur", (e) => {
  //   console.log(municipios.value);

  fetch(
    `https://servicodados.ibge.gov.br/api/v1/localidades/estados/${municipios.value}/municipios`
  )
    .then((response) => {
      response.json().then((data) => dadosDoEstado(data));
      //   console.log(response);
    })
    .catch((e) => console.log("Deu Erro: " + e));
});
