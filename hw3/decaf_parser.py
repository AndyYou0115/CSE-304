'''
Name: Li Xing Liu
Netid: lixiliu
Student Id: 113318331

Name: Andy You
Netid: Andyou
Student Id: 113494190
'''

import sys
from decaf_lexer import *
from decaf_ast import *
# program ::= class_decl* 
# this means that the program consists of zero or more classes

precedence = (
    ('right', '='),
    ('left', 'BOOL_OR'),
    ('left', 'BOOL_AND'),
    ('nonassoc', 'EQUALITY', 'DISQUALITY'),
    ('nonassoc', 'GREATERTHAN', 'LESSTHAN', 'LEQ', 'GEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'NOT', 'UMINUS', "UPLUS")
)


def p_program(p):
    '''program : class_decl_list'''
    p[0] = Program(p[1])
    return True
     
def p_class_decl_list(p):
    '''class_decl_list : class_decl class_decl_list
                    | empty'''
    pass

def p_class_decl(p):
    '''class_decl : CLASS ID EXTENDS ID '{' class_body_decl '}'
                | CLASS ID '{' class_body_decl '}' '''
    pass
    
def p_class_body_decl(p):
    '''class_body_decl : field_decl
                        | method_decl
                        | constructor_decl
                        | class_body_decl field_decl
                        | class_body_decl method_decl
                        | class_body_decl constructor_decl'''
    pass

def p_field_decl(p):
    '''field_decl : modifier var_decl'''
    pass

def p_modifier(p):
    '''modifier : PUBLIC STATIC
            | PRIVATE STATIC
            | PUBLIC
            | PRIVATE
            | STATIC
            | empty'''
def p_var_decl(p):
    '''var_decl : type variables ';' '''
    pass

def p_type(p):
    '''type : INT
        | FLOAT
        | BOOLEAN
        | ID'''
    pass

def p_variables(p):
    '''variables : variable variables_cont'''
    pass

def p_variables_cont(p):
    '''variables_cont : ',' variable variables_cont
		                | empty'''
    pass

def p_variable(p):
    '''variable : ID'''
    pass
            
def p_method_decl(p):
    '''method_decl : modifier type ID LEFTPAREN formals RIGHTPAREN block
				| modifier VOID ID LEFTPAREN formals RIGHTPAREN block'''
    pass

def p_constructor_decl(p):
    '''constructor_decl : modifier ID LEFTPAREN formals RIGHTPAREN block'''
    pass

def p_formals(p):
    '''formals : formal_param formals_cont
            | empty'''
    pass

def p_formals_cont(p):
    '''formals_cont : ',' formal_param formals_cont
            | empty'''
    pass

def p_formal_param(p):
    '''formal_param : type variable'''
    pass

def p_block(p):
    '''block : '{' stmt_list '}' '''
    pass

def p_stmt_list(p):
    ''' stmt_list : stmt stmt_list
                | empty '''
    pass

def p_stmt(p):
    '''stmt : IF LEFTPAREN expr RIGHTPAREN stmt
            | IF LEFTPAREN expr RIGHTPAREN stmt ELSE stmt
            | WHILE LEFTPAREN expr RIGHTPAREN stmt 
            | FOR LEFTPAREN for_cond_1 ';' for_cond_2 ';' for_cond_3 RIGHTPAREN stmt
            | RETURN return_val ';'
            | stmt_expr ';'
            | BREAK ';'
            | CONTINUE ';'
            | block
            | var_decl
            | ';' '''
    pass

def p_for_cond_1(p):
    '''for_cond_1 : stmt_expr
                | empty'''
    pass

def p_for_cond_2(p):
    '''for_cond_2 : expr
                | empty'''
    pass

def p_for_cond_3(p):
    '''for_cond_3 : stmt_expr
                | empty'''
    pass

def p_return_val(p):
    '''return_val : expr
                | empty'''
    pass

def p_literal(p):
    '''literal : INT_CONST
                | FLOAT_CONST
                | STRING_CONST
                | NULL
                | TRUE
                | FALSE'''
    
def p_primary(p):
    '''primary : literal
                | THIS
                | SUPER
                | LEFTPAREN expr RIGHTPAREN 
                | NEW ID LEFTPAREN arguments RIGHTPAREN
                | lhs
                | method_invocation '''
    pass
def p_arguments(p):
    ''' arguments : expr arguments_cont
            | empty '''
    pass

def p_arguments_cont(p):
    ''' arguments_cont : ',' expr arguments_cont 
                    | empty '''
    pass

def p_lhs(p):
    '''lhs : field_access'''         
    pass

def p_field_access(p):
    '''field_access : primary '.' ID
                    | ID'''
    pass

def p_method_invocation(p):
    ''' method_invocation : field_access LEFTPAREN arguments RIGHTPAREN '''
    pass

def p_expr(p):
    '''expr : primary
            | assign'''
pass

def p_assign(p):
    '''assign : lhs '=' expr
                | lhs INCREMENT
                | INCREMENT lhs 
                | lhs DECREMENT
                | DECREMENT lhs'''
    pass

def p_add_expr(p):
    '''expr : expr PLUS expr'''
    pass
def p_sub_expr(p):
    '''expr : expr MINUS expr'''
    pass

def p_mult_expr(p):
    '''expr : expr MULTIPLY expr'''
    pass

def p_div_expr(p):
    '''expr : expr DIVIDE expr '''
    pass

def p_conj_expr(p):
    '''expr : expr BOOL_AND expr'''
    pass

def p_disj_expr(p):
    '''expr : expr BOOL_OR expr'''
    pass

def p_equals_expr(p):
    '''expr : expr EQUALITY expr'''
    pass

def p_notequals_expr(p):
    '''expr : expr DISQUALITY expr'''
    pass

def p_lt_expr(p):
    '''expr : expr LESSTHAN expr'''
    pass

def p_lte_expr(p):
    '''expr : expr LEQ expr'''
    pass

def p_gt_expr(p):
    '''expr : expr GREATERTHAN expr'''
    pass

def p_gte_expr(p):
    '''expr : expr GEQ expr'''
    pass

def p_pos_expr(p):
    '''expr : PLUS expr %prec UPLUS'''
    pass

def p_minus_expr(p):
    '''expr : MINUS expr %prec UMINUS'''
    pass

def p_not_expr(p):
    '''expr : NOT expr'''
    pass
def p_stmt_expr(p):
    '''stmt_expr : assign
                | method_invocation'''
    
def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print()
    if p:
        if not hasattr(p.lexer, "lineStart"): 
            print("Syntax error at '%s' (%d, %d)" %
          		(p.value, p.lineno, p.lexpos))
            sys.exit()
        print("Syntax error at '%s' (%d, %d)" %
          (p.value, p.lineno, p.lexpos - p.lexer.lineStart))
        print("Syntax error at token,", p.type, ", line", p.lineno)
    else:
        print("Syntax error at EOF")
    print()
    sys.exit()
    
				


                

