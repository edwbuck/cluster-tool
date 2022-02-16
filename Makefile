DISTRO=$(shell lsb_release -si)

package:
	@make -C packaging/$(DISTRO) $@

clean:
	@make -C packaging/$(DISTRO) $@
