import module
assert module.pascalize('test_metni') == 'TestMetni'
assert module.pascalize('şimşek sokağı') == 'ŞimşekSokağı'
assert module.depascalize('TestMetni') == 'test_metni'
assert module.depascalize('ŞimşekSokağı') == 'şimşek_sokağı'
assert module.camelize('Lorem ipsum dolor sit amet.') == 'loremIpsumDolorSitAmet.'
assert module.camelize('Mrs. Dalloway çiçekleri kendi alacaktı.') == 'mrsDallowayÇiçekleriKendiAlacaktı'
assert module.camelize('mrsDallowayÇiçekleriKendiAlacaktı') == 'mrs_dalloway_çiçekleri_kendi_alacaktı'
assert module.is_pascalize('TestMetni') == True
assert module.is_camelcase('LoremIpsumDolorSitAmet') == False
assert module.is_snakecase('test_metni') == True

#Since there is no punctuation check in the Camel case control, I did not add the relevant case in my code.
#It gives an error because the dot is deleted in the 7th line, it gives an error because "_" is added in the 8th line.