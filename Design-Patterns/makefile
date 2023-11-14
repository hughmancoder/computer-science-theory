JAVAC=/usr/bin/javac
JAVA=/usr/bin/java
BINDIR=bin

# Strategy Pattern Sources and Targets
STRATEGY_SOURCES=$(wildcard Strategy/ducks/*.java Strategy/ducks/behaviours/*.java)
STRATEGY_TARGET=$(BINDIR)/StrategyPattern

# Observer Pattern Sources and Targets
OBSERVER_SOURCES=$(wildcard Observer/weatherStation/*.java Observer/weatherStation/weather/*.java Observer/weatherStation/observers/*.java Observer/weatherStation/weather/subscribers/*.java)
OBSERVER_TARGET=$(BINDIR)/ObserverPattern

all: strategy observer

# Strategy Pattern Rules
strategy: $(STRATEGY_TARGET)

$(STRATEGY_TARGET): $(STRATEGY_SOURCES)
	$(JAVAC) -d $(BINDIR) $^

run-strategy-pattern: strategy
	$(JAVA) -cp $(BINDIR) Main

# Observer Pattern Rules
observer: $(OBSERVER_TARGET)

$(OBSERVER_TARGET): $(OBSERVER_SOURCES)
	$(JAVAC) -d $(BINDIR) $^

run-observer-pattern: observer
	$(JAVA) -cp $(BINDIR) Main

clean:
	rm -rf $(BINDIR)/*

.PHONY: strategy observer clean
