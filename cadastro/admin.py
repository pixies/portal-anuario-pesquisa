# -*- coding: utf-8 -*-

from django.contrib import admin
from cadastro.models import *
# Register your models here.

class TituloAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ['id', 'nome']

class TitulacaoTabularAdmin(admin.TabularInline):
	model = Titulacao
	extra = 0

class AreaFormacaoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ['id', 'nome']

class FormacaoTabularAdmin(admin.TabularInline):
	model = Formacao
	extra = 0

class CursoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ['id', 'nome']

class CursoVinculadoTabularAdmin(admin.TabularInline):
	model = CursoVinculado
	extra = 0

class PesquisadorAdmin(admin.ModelAdmin):

	list_display = ('id', 'nome', 'sexo', 'email')
	list_filter = ['titulos__nome', 'cursos_vinculados__nome']

	search_fields = ['nome', 'id']

	fieldsets = [
		('Informações Pessoais', {'fields': ['nome', 'sexo', 'email']}),
		('Informações Acadêmicas', {'fields': ['nome_cientifico', 'url_lates']}),
	]

	inlines = [TitulacaoTabularAdmin, FormacaoTabularAdmin, CursoVinculadoTabularAdmin]



class InstituicaoSubmissaoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ['id', 'nome']

class FonteFinanciamentoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ['id', 'nome']

class InstituicaoCooperadoraAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ['id', 'nome']

class CooperacaoTabularAdmin(admin.TabularInline):
	model = Cooperacao
	extra = 0

class AreaConhecimentoAdmin(admin.ModelAdmin):
	list_display = ['id', 'nome']
	search_fields = ['id', 'nome']

class AreaRelacionadaTabularAdmin(admin.TabularInline):
	model = AreaRelacionada
	extra = 0

class LocalAdmin(admin.ModelAdmin):
	list_display = ['codigo_ibge', 'descricao','nome_cidade', 'pais']
	search_fields = ['codigo_ibge', 'descricao', 'nome_cientificocidade']
	list_filter = ['pais', 'nome_cidade']

class LocalPesquisaTabularAdmin(admin.TabularInline):
	model = LocalPesquisa
	extra = 0

class PalavraChaveAdmin(admin.ModelAdmin):
	list_display = ('id', 'palavra')
	search_fields = ('id', 'palavra')

class PalavraChavePesquisaTabularAdmin(admin.TabularInline):
	model = PalavraChavePesquisa
	extra = 5
	#raw_id_fields = ('palavra_chave',)

class ParticipacaoAutoralTabularAdmin(admin.TabularInline):
	model = ParticipacaoAutoral
	extra = 3
	raw_id_fields = ('pesquisador',)

class PesquisaAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'status')
	search_fields = ['id', 'titulo', 'palavras_chave__palavra', 'areas_conhecimento__nome']
	list_filter = ['tipo', 'status', 'data_submissao','instituicao_submissao__nome', 'fonte_financiamento__nome', 'areas_conhecimento__nome',]
	#raw_id_fields = ('instituicao_submissao', 'fonte_financiamento')

	fieldsets = [
		('Informações da pesquisa', {'fields': [
				'titulo',
				'tipo',
				'status',
				'tempo_duracao',
				'impacto_pesquisa',
				'qualificacao',
				'gerou_patente',
				'instituicao_submissao',
				'fonte_financiamento',
				'resumo',
				'url_submissao',
				'data_submissao',
		]}),
	]

	inlines = [ParticipacaoAutoralTabularAdmin, CooperacaoTabularAdmin, AreaRelacionadaTabularAdmin, LocalPesquisaTabularAdmin, PalavraChavePesquisaTabularAdmin]

admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(Titulo, TituloAdmin)
admin.site.register(AreaFormacao, AreaFormacaoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Pesquisa, PesquisaAdmin)
admin.site.register(InstituicaoSubmissao, InstituicaoSubmissaoAdmin)
admin.site.register(InstituicaoCooperadora, InstituicaoCooperadoraAdmin)
admin.site.register(FonteFinanciamento, FonteFinanciamentoAdmin)
admin.site.register(AreaConhecimento, AreaConhecimentoAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(PalavraChave, PalavraChaveAdmin)

#admin.site.register(Titulacao)