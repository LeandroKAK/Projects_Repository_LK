package br.ceub.desenvolvimento.aula02;

import java.util.ArrayList;

public class CadastroAlunos {
    private ArrayList<Aluno> alunos = new ArrayList<>();
    public void adicionar(Aluno aluno) {
        alunos.add(aluno);
    }
    public String listarTodos() {
        if (alunos.isEmpty()) {
            return "Nenhum aluno cadastrado.";
        }
        String resultado = "";
        for (Aluno aluno : alunos) {
            resultado += aluno.gerarResumo() + "\n";
        }
        return resultado;
    }
    public Aluno buscarPorNome(String nome) {
        for (Aluno aluno : alunos) {
            if (aluno.getNome().equalsIgnoreCase(nome)) {
                return aluno;
            }
        }      
        return null;
    }
    public Aluno buscarPorSemestre(int semestre) {
        for (Aluno aluno : alunos) {           
            if (aluno.getSemestre() == semestre) {
                return aluno;
            }
        }
        return null;
    }
    public int quantidade() {
        return alunos.size();
    }
}