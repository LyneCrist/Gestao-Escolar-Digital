from http import client
from unicodedata import numeric
from django.test import TestCase
from common.util import CommonsUtil


class PacienteFormTestCase(TestCase, CommonsUtil):

    def setUp(self) -> None:

        self.paciente_ok = {
            "nome": "Tatiane Eliane Aparício",
            "telefone": "+55(62) 98833-9109",
            "cartao_sus": "237186420750009",
        }

        self.paciente_nok = {
            "nome": "Tatiane Eliane. Aparício",
            "telefone": "+55(62) +._=98833-91509",
            "cartao_sus": "237186420750.A009+",
        }

    def test_acerto_verifica_se_cartao_sus_existe(self):

        self.assertIsNotNone(self.paciente_ok["cartao_sus"], "Campo obrigatório")

    def test_acerto_verifica_tamanho_de_campo_cartao_sus(self):

        self.assertEqual(
            len(self.paciente_ok["cartao_sus"]),
            15,
            "Campo deve possuir um tamanho de 15 dígitos",
        )

    def test_acerto_verifica_formato_de_campo_cartao_sus(self):

        self.assertIsNotNone(
            self.is_numeric_pattern(self.paciente_ok["cartao_sus"]),
            "Formato de campo inválido, informe apenas números",
        )

    def test_acerto_no_tamanho_campo_telefone(self) -> None:

        self.assertEqual(
            len(self.remove_characters(self.paciente_ok["telefone"])),
            13,
            "Tamanho inválido para telefone",
        )

    def test_acerto_remove_caracteres_alpha(self) -> None:

        self.assertEqual(
            self.remove_characters(self.paciente_ok["telefone"]),
            "5562988339109",
            "Formato inválido para telefone",
        )

    def test_acerto_verifica_formato_telefone(self) -> None:

        self.assertIsNotNone(
            self.is_phone_pattern(self.remove_characters(self.paciente_ok["telefone"])),
            "Formato inválido para telefone",
        )

    def test_falha_no_formato_campo_nome(self) -> None:

        self.assertIsNone(self.is_alpha_pattern(self.paciente_nok["nome"]))

    def test_falha_no_tamanho_campo_telefone(self) -> None:

        self.assertFalse(
            len(self.remove_characters(self.paciente_nok["telefone"])) == 13
        )

    def test_falha_no_formato_campo_telefone(self) -> None:

        self.assertIsNone(self.is_phone_pattern(self.paciente_nok["telefone"]))
