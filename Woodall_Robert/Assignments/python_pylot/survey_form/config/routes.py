from system.core.router import routes

routes['default_controller'] = 'Surveys'
routes['POST']['/surveys/process'] = 'Surveys#process'
routes['GET']['/result'] = 'Surveys#display_result'
routes['GET']['/reset'] = 'Surveys#reset_session'