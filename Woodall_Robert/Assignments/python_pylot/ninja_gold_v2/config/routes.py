from system.core.router import routes

routes['default_controller'] = 'NinjaGold'
routes['POST']['/process_gold'] = 'NinjaGold#process_gold'
routes['GET']['/reset'] = 'NinjaGold#reset'
