import React from 'react';
import './App.css';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      transacoesList: [],
      activeItems: {
        id: null,
        Tipo: '',
        Data: '',
        Valor: '',
        CPF: '',
        Cartao: '',
        Hora: '',
        Dono_da_Loja: '',
        Nome_da_Loja: '',
        Total: '',
        Sinal:''
      },
      editing: false
    }
    this.fetchTransacoes = this.fetchTransacoes.bind(this)
  };

  componentWillMount() {
    this.fetchTransacoes()

  }

  fetchTransacoes() {

    fetch('http://127.0.0.1:8000/api/transacoes-lista/')
      .then(response => response.json())
      .then(data =>
        this.setState({
          transacoesList: data
        })
      )
  }

  render() {
    var transacoes = this.state.transacoesList
    return (
      <>
      <div className="container">
        <div>
          <h1>Operações importadas por lojas</h1>
        </div>
        <div className="transacao">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Tipo da transação</th>
                <th scope="col">Data da ocorrência</th>
                <th scope="col">Valor da movimentação</th>
                <th scope="col">CPF do beneficiário</th>
                <th scope="col">Cartão utilizado na transação</th>
                <th scope="col">Hora da ocorrência</th>
                <th scope="col">Nome do representante da loja</th>
                <th scope="col">Nome da loja</th>
                <th scope="col">Total</th>
              </tr>
            </thead>
            <tbody>
              {transacoes.map(function (transacao, index) {
               return (<tr key={index}>
                  <td>{transacao.Tipo}</td>
                  <td>{transacao.Data}</td>
                  <td>{transacao.Total.Sinal}{transacao.Valor}</td>
                  <td>{transacao.CPF}</td>
                  <td>{transacao.Cartao}</td>
                  <td>{transacao.Hora}</td>
                  <td>{transacao.Dono_da_Loja}</td>
                  <td>{transacao.Nome_da_loja}</td>
                  <td>{transacao.Total}</td>
                </tr>)
              })}
            </tbody>
          </table>
        </div>
      </div>
      </>
    )
  }
}

export default App;
